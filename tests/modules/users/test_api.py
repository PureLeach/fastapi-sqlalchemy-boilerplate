

async def test_create_user(test_client, db):
    response = await test_client.post('/users/', json={"name": "my_name"})
    result = response.json()
    print(f'\033[32m result, { result }, {type(result)} \033[0m')
    

async def test_get_users(test_client, db):
    response = await test_client.get('/users/')
    result = response.json()
    print(f'\033[32m result, { result }, {type(result)} \033[0m')
