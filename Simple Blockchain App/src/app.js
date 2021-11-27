App = {

    loading: false,
    contracts: {},

    // Chức năng khi trang web tải
    load: async () => {

        console.log("App loading...");
        await App.loadWeb3();
        await App.loadAccount();
        await App.loadContract();
        await App.render();

    },

    // Chức năng tải Web3.js, framework sẽ hoạt động với MetaMask để tạo Ethereum Blockchain Network
    loadWeb3: async () => {

        if(typeof web3 !== 'undefined') {
            App.web3Provider = web3.currentProvider;
            web3 = new Web3(web3.currentProvider);
        } else {
            windows.alert("Please connect to Metamask.");
        }

        // trình duyệt hiện đại
        if(window.ethereum) {
            window.web3 = new Web3(ethereum);

            try {
                // Yêu cầu quyền truy cập tài khoản
                await ethereum.enable();

                // Tài khoản hiện đã được công khai
                web3.eth.sendTransaction({ /* ... */ });
            } catch(error) {
                // Người dùng từ chối quyền truy cập tài khoản
            }
        }

        // Trình duyệt kế thừa
        else if(window.web3) {
            App.web3Provider = web3.currentProvider;
            window.web3 = new Web3(web3.currentProvider);

            // Tài khoản hiện đã được công khai
            web3.eth.sendTransaction({ /* ... */ });
        }

        // Không phải là một ETH Browser
        else {
            console.log("Non ETH Browser detected.")
        }

    },

    loadAccount: async () => {

        // Tài khoản thứ nhất
        App.account = web3.eth.accounts[0];

    },

    loadContract: async () => {

        // Hợp đồng thôgn minh
        const todoList = await $.getJSON('TodoList.json');
        App.contracts.TodoList = TruffleContract(todoList);
        App.contracts.TodoList.setProvider(App.web3Provider);

        // Lấy các giá trị từ blockchain
        App.todoList = await App.contracts.TodoList.deployed();

    },

    render: async () => {

        if(App.loading) {
            return;
        }

        // Đặt trạng thái tải thành true
        App.setLoading(true);

        // Kết xuất tài khoản
        $('#account').html(App.account);

        // Kết xuất công việc
        await App.renderTasks();

        // Cập nhật trạng thái tải thành false
        App.setLoading(false);

    },

    renderTasks: async () => {

        // Load task từ blockchain
        const taskCount = await App.todoList.taskCount();
        const $taskTemplate = $('.taskTemplate');

        // Kết xuất từng task dưới dạng mẫu
        for(var i = 1; i <= taskCount; i++) {

            // Nạp tác vụ từ chuỗi khối
            const task = await App.todoList.tasks(i);
            const taskId = task[0].toNumber();
            const taskContent = task[1];
            const taskCompleted = task[2];

            // Tạo mẫu HTML cho task
            const $newTaskTemplate = $taskTemplate.clone();
            $newTaskTemplate.find('.content').html(taskContent);
            $newTaskTemplate.find('input')
                            .prop('name', taskId)
                            .prop('checked', taskCompleted)
                            .on('click', App.toggleCompleted);

            // Định dạng các task theo đúng thứ tự
            if(taskCompleted) {
                // Assign the id #completedTaskList to the template
                $('#completedTaskList').append($newTaskTemplate);
            } else {
                // gán #taskList id đến biểu mẫu
                $('#taskList').append($newTaskTemplate);
            }

            // Show task
            $newTaskTemplate.show();

        }
    },

    createTask: async () => {

        // Đặt trạng thái tải thành true
        App.setLoading(true);

        // Lấy giá trị của biểu mẫu
        const content = $('#newTask').val();

        // Tạo task từ Hợp đồng thông minh(Smart Contract)
        await App.todoList.createTask(content);

        // Tải lại trang
        window.location.reload();

    },

    toggleCompleted: async(e) => {

        // Đặt trạng thái tải thành true
        App.setLoading(true);

        // Lấy id từ mục checkbox
        const taskId = e.target.name;

        // Chỉnh sửa task
        await App.todoList.toggleCompleted(taskId);

        // Tải lại tranng
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
