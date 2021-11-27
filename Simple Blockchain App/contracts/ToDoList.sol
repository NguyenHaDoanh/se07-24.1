pragma solidity ^0.5.0;

contract TodoList {

    // Uint => số nguyên >= 0
    // Khóa công khai(public key), để sử dụng biến giống như một hàm (ex: this.taskCount() = 0)

    uint public taskCount = 0;
    
    struct Task {
        uint id;
        string content;
        bool completed;
    }

    // Sắp xếp mảng, Task là một uint
    mapping(uint => Task) public tasks;

    // Định nghĩa event TaskCreated 
    event TaskCreated(
        uint id, 
        string content,
        bool completed
    );

    // Định nghĩa event TaskCompleted
    event TaskCompleted(
        uint id,
        bool completed
    );

    // Function that runs the first time that the script start, as a configurator
    constructor() public {

        // Create an default task for the first compile
        createTask("Default task.");
        
    }

    // Function to add in the "tasks" array a new task
    function createTask(string memory _content) public {

        // Increment taskCount + 1 to assign an ID
        taskCount ++;

        // Adding to the task array a new task
        tasks[taskCount] = Task(taskCount, _content, false);

        // Emit TaskCreated event
        emit TaskCreated(taskCount, _content, false);

    }

    // Function to complete tasks and target as completed: true
    function toggleCompleted(uint _id) public {

        // Assign at _task the value of tasks[_id]
        Task memory _task = tasks[_id];

        // Assign true/false to the task
        _task.completed = !_task.completed;

        // Assign to the array item the new edited task
        tasks[_id] = _task;

        // Emitting TaskCompleted
        emit TaskCompleted(_id, _task.completed);

    }

}
