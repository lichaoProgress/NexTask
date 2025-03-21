import pytest
import requests

BASE_URL = "http://127.0.0.1:8099"



# 登录并获取 Token
def get_auth_token():
    login_data = {
        "account": "lichao",  
        "password": "123456" 
    }
    response = requests.post(f"{BASE_URL}/api/v1/users/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    token = data["data"]["token"]
    print("token: ",token)
    assert token is not None
    return token

# 获取带有 Token 的请求头
def get_headers():
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}"
    }





# 测试用户登录
def test_login():
    response = requests.post(f"{BASE_URL}/api/v1/users/login", json={"account": "lichao", "password": "123456"})
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["code"] == "000-0000"
    assert data["message"] == "SUCCESS"
    assert "token" in data["data"]


# # 测试用户注册  
def test_register():
    json_data = {
        
        "username": "admin",
        "password": "123456",
        "email": "admin@example.com",
        "phone": "13245698547",
        "github_uid": 0
    }

    response = requests.post(f"{BASE_URL}/api/v1/users/register", json=json_data)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["code"] == "000-0000"
    assert data["message"] == "SUCCESS"
    assert "token" in data["data"]


# 测试创建任务  
def test_create_task():
    task_data = {
        "project_name": "任务1",
        "project_desc": "任务1",
        "project_status": "todo",
        "project_type": 0,
        "project_priority": "medium",
        "start_time": "2025-03-21T04:19:43.845Z",
        "end_time": "2025-03-21T04:19:43.845Z",
        "project_tags": [],
        "project_icon": ""
        }
    headers = get_headers()
    response = requests.post(f"{BASE_URL}/api/v1/projects", json=task_data,headers=headers)
    assert response.status_code == 200
    task = response.json()
    print(task)
    # {'code': '000-0000', 'message': 'SUCCESS', 'data': {'id': 9}}
    assert task["code"] == "000-0000"
    assert task["message"] == "SUCCESS"


# 测试获取分页任务列表   
def test_get_tasks():
    headers = get_headers()
    params = {
        "current_page": 1,
        "page_size": 100,
        "project_name": "待办",
        "project_priority": "medium",
        "project_status": "todo"
    }
    response = requests.get(f"{BASE_URL}/api/v1/projects", headers=headers,params=params)
    assert response.status_code == 200
    tasks = response.json()
    print(tasks)
    assert tasks["code"] == "000-0000"
    assert tasks["message"] == "SUCCESS"
    assert isinstance(tasks["data"]["data_list"], list)

# 测试获取单个任务  
def test_get_single_task():
    # task_id = test_create_task()  # 先创建一个任务
    headers = get_headers()
    params = {
        "current_page": 1,
        "page_size": 100,
        "id": 10
    }
    response = requests.get(f"{BASE_URL}/api/v1/projects/detail", params=params,headers=headers)
    assert response.status_code == 200
    task = response.json()
    print(task)
    assert task["code"] == "000-0000"
    assert task["message"] == "SUCCESS"

# 测试更新任务  
def test_update_task():
    # task_id = test_create_task()  # 先创建一个任务
    headers = get_headers()
    updated_data =  {
        "id": 9,
        "project_name": "任务111",
        "project_desc": "任务111",
        "project_status": "todo",
        "project_type": 0,
        "project_priority": "medium",
        "start_time": "2025-03-21T04:19:43.845Z",
        "end_time": "2025-03-21T04:19:43.845Z",
        "project_tags": [],
        "project_icon": ""
        }
    task_id = 9
    response = requests.put(f"{BASE_URL}/api/v1/projects/{task_id}", json=updated_data,headers=headers)
    assert response.status_code == 200
    task = response.json()
    print(task)
    assert task["code"] == "000-0000"
    assert task["message"] == "SUCCESS"

# 测试删除任务   
def test_delete_task():
    headers = get_headers()
    # task_id = test_create_task()  # 先创建一个任务
    data = {
        "project_ids": [9]
    }
    response = requests.delete(f"{BASE_URL}/api/v1/projects/",headers=headers,json=data)
    assert response.status_code == 200
    task = response.json()
    print(task)
    assert task["code"] == "000-0000"
    assert task["message"] == "SUCCESS"

# 运行测试
if __name__ == "__main__":
    pytest.main()
