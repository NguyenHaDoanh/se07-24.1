App = {

    loading: false,
    contracts: {},

    // Function when the website loads
    load: async () => {

        console.log("App loading...");
        await App.loadWeb3();
        await App.loadAccount();
        await App.loadContract();
        await App.render();

    },

    // Function to load Web3.js, framework that will works with MetaMask to create the Ethereum Blockchain Network
    loadWeb3: async () => {

        if(typeof web3 !== 'undefined') {
            App.web3Provider = web3.currentProvider;
            web3 = new Web3(web3.currentProvider);
        } else {
            windows.alert("Please connect to Metamask.");
        }

        // Modern browsers
        if(window.ethereum) {
            window.web3 = new Web3(ethereum);

            try {
                // Request account access
                await ethereum.enable();

                // Account now exposed
                web3.eth.sendTransaction({ /* ... */ });
            } catch(error) {
                // User denied the account access
            }
        }

        // Legacy browsers
        else if(window.web3) {
            App.web3Provider = web3.currentProvider;
            window.web3 = new Web3(web3.currentProvider);

            // Account now exposed
            web3.eth.sendTransaction({ /* ... */ });
        }

        // Not an ETH Browser
        else {
            console.log("Non ETH Browser detected.")
        }

    },

    loadAccount: async () => {

        // The first account
        App.account = web3.eth.accounts[0];

    },

    loadContract: async () => {

        // The smart contracts
        const todoList = await $.getJSON('TodoList.json');
        App.contracts.TodoList = TruffleContract(todoList);
        App.contracts.TodoList.setProvider(App.web3Provider);

        // Take values from blockchain
        App.todoList = await App.contracts.TodoList.deployed();

    },

    render: async () => {

        if(App.loading) {
            return;
        }

        // Set loading state to true
        App.setLoading(true);

        // Render account
        $('#account').html(App.account);

        // Render tasks
        await App.renderTasks();

        // Updating loading state to false
        App.setLoading(false);

    },

    renderTasks: async () => {

        // Load the task from the blockchain
        const taskCount = await App.todoList.taskCount();
        const $taskTemplate = $('.taskTemplate');

        // Render each task as a template
        for(var i = 1; i <= taskCount; i++) {

            // Fetch task from the blockchain
            const task = await App.todoList.tasks(i);
            const taskId = task[0].toNumber();
            const taskContent = task[1];
            const taskCompleted = task[2];

            // Create the HTML template for the task
            const $newTaskTemplate = $taskTemplate.clone();
            $newTaskTemplate.find('.content').html(taskContent);
            $newTaskTemplate.find('input')
                            .prop('name', taskId)
                            .prop('checked', taskCompleted)
                            .on('click', App.toggleCompleted);

            // Format the tasks in the correct order
            if(taskCompleted) {
                // Assign the id #completedTaskList to the template
                $('#completedTaskList').append($newTaskTemplate);
            } else {
                // Assign the #taskList id to the template
                $('#taskList').append($newTaskTemplate);
            }

            // Show the task
            $newTaskTemplate.show();

        }
    },

    createTask: async () => {

        // Set loading state to true
        App.setLoading(true);

        // Take the form's value
        const content = $('#newTask').val();

        // Create the task from the Smart Contract
        await App.todoList.createTask(content);

        // Reload the page
        window.location.reload();

    },

    toggleCompleted: async(e) => {

        // Set loading state to true
        App.setLoading(true);

        // Take the checkbox item id
        const taskId = e.target.name;

        // Edit the task
        await App.todoList.toggleCompleted(taskId);

        // Reload the page
        window.location.reload();

    },

    setLoading: (boolean) => {

        App.loading = boolean;
        const loader = $('#loader');
        const content = $('#content');

        if(boolean) {
            loader.show();
            content.hide();
        } else {
            loader.hide();
            content.show();
        }

    },

}

$(() => {
    $(window).load(() => {
        App.load();
    })
})
