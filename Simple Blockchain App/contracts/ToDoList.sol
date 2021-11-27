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

    // Hàm chạy lần đầu khi tập lệnh(script) bắt đầu, như là một configurator
    constructor() public {

        // Tạo một tác vụ mặc định cho lần biên dịch đầu tiên
        createTask("Default task.");
        
    }

    // Hàm để thêm vào mảng "tasks" một nhiệm vụ mới
    function createTask(string memory _content) public {

        // tăng taskCount +1 để chỉ định 1 id
        taskCount ++;

        // thêm vào mảng task 1 task mới
        tasks[taskCount] = Task(taskCount, _content, false);

        // Emit TaskCreated event
        emit TaskCreated(taskCount, _content, false);

    }

    // Chức năng hoàn thành nhiệm vụ và hoàn thành mục tiêu: true
    function toggleCompleted(uint _id) public {

        // Gán _task giá trị của tasks[_id]
        Task memory _task = tasks[_id];

        // Gán True/False cho task
        _task.completed = !_task.completed;

        // Gán cho item của array một task vừa được chỉnh sửa
        tasks[_id] = _task;

        // Emitting TaskCompleted
        emit TaskCompleted(_id, _task.completed);

    }

}
