const TodoList = artifacts.require("./TodoList.sol");
// Kiểm tra danh sách việc cần làm


contract('TodoList', (accounts) => {
    // Hiển thị các tài khoản trong blockchain

    before(async () => {
        this.todoList = await TodoList.deployed();
        // Mỗi lần chạy có 1 bản sao việc cần làm khi triển khai các chuỗi block
    });

    it('deploys successfully', async () => {
        const address = await this.todoList.address;
        assert.notEqual(address, 0x0);
        assert.notEqual(address, '');
        assert.notEqual(address, null);
        assert.notEqual(address, undefined);
        // kiểm tra xem hợp đồng đã được triển khai vào blockchain đúng cách hay chưa bằng cách kiểm tra địa chỉ của nó.
    });

    it('lists tasks', async () => {
        const taskCount = await this.todoList.taskCount();
        const task = await this.todoList.tasks(taskCount);
        assert.equal(task.id.toNumber(), taskCount.toNumber());
        assert.equal(task.content, 'Chiamarsi Fra');
        assert.equal(task.completed, false);
        assert.equal(taskCount.toNumber(), 1);
    });
    //  kiểm tra xem hợp đồng thông minh có liệt kê nhiệm vụ đúng cách hay không 

    it('creates tasks', async() => {
        const result = await this.todoList.createTask('A new task');
        const taskCount = await this.todoList.taskCount();
        assert.equal(taskCount, 2);
        
        const event = result.logs[0].args;
        assert.equal(event.id.toNumber(), 2);
        assert.equal(event.content, 'A new task');
        assert.equal(event.completed, false);
        // kiểm tra để đảm bảo rằng sự kiện này được kích hoạt bất cứ khi nào một tác vụ mới được tạo
        // đảm bảo rằng sự kiện đã được kích hoạt đúng cách
    });
    

    it('toggles task completion', async () => {
        const result = await this.todoList.toggleCompleted(1);
        const task = await this.todoList.tasks(1);
        assert.equal(task.completed, true);
        
        const event = result.logs[0].args;
        assert.equal(event.id.toNumber(), 1);
        assert.equal(event.completed, true);
        
        //Đánh dấu hoàn thành công việc
    })

});
