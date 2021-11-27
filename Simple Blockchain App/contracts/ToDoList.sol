// pragma solidity ^0.5.0;

contract TodoList {

    // Uint => số nguyên >= 0  //in ko dau
    // Khóa công khai(public key), để sử dụng biến giống như một hàm (ex: this.taskCount() = 0)

    uint public taskCount = 0;
    
    struct Task { ////biến struct cho phép chúng ta xác định nhiều cấu trúc data hơn.
        uint id;
        string content; ////đây là văn bản của nhiệm vụ trong danh sách việc cần làm được chứa trong một chuỗi.
        bool completed;// Nếu đúng như vậy--> true, 
                        //nhiệm vụ sẽ được "hoàn thành" hoặc sẽ bị đánh dấu khỏi danh sách việc cần làm.
    }

    // Ánh xạ)) Sắp xếp mảng, Task là một uint 
    mapping(uint => Task) public tasks;

    // Định nghĩa event TaskCreated 
    // Xác định sự kiện TaskCreate taskcreated : nhiem v u tao ra
    event TaskCreated(
        uint id, 
        string content,
        bool completed
    );
// nó lưu trữ các đối số được truyền vào nhật ký giao dịch

    // Define the TaskCompleted event xác định
    event TaskCompleted(
        uint id,
        bool completed
    );

    // Hàm chạy lần đầu khi tập lệnh(script) bắt đầu, như là một configurator
    constructor() public {

        // Tạo một tác vụ mặc định cho lần biên dịch đầu tiên
        createTask("Default task.");//Default task : nhiệm vụ mặc định
        
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

        // Gán cho item của array một task vừa được chỉnh sửa (chỉ mục mới)
        tasks[_id] = _task;

        // Emitting TaskCompleted
        emit TaskCompleted(_id, _task.completed);

    }

}
