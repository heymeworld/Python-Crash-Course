#!/usr/bin/env python
# coding: utf-8

# # Assessment - Object-oriented programming

# In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections. 
# <br><br>
# To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server.  For our simulation, each connection creates a random amount of load in the server, between 1 and 10.
# <br><br>
# Run the following code that defines this Server class.

# In[74]:


#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        # 생성자 호출, Dict 타입의 멤버 변수  
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        # 커넥션을 서버에 추가하는 메서드

        # 변수를 난수로 초기화 (겹치지 않는 수가 필요한 듯 싶다)
        connection_load = random.random()*10+1
        
        # Add the connection to the dictionary with the calculated load
        # id : load 로 딕셔너리에 추가
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # 딕셔너리에서 연결 정보를 제거하는 메서드
        
        # Remove the connection from the dictionary
        # 딕셔너리 요소 제거
        del self.connections[connection_id]
        
    def load(self):
        """Calculates the current load for all connections."""
        # 로드 변수에 저장된 값들을 계산, 커넥션의 수를 계산하는 것이 아님
        total = 0
        
        # Add up the load for each of the connections
        # 딕셔너리 value 요소들만 빼내서 전부 더 하기
        for connection in self.connections.values():
            total += connection
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        # 해당 클래스의 객체를 프린트하면 나올 메세지 정의
        # 로드 값 합계 출력
        return "{:.2f}%".format(self.load())
    
#End Portion 1#


# Now run the following cell to create a Server instance and add a connection to it, then check the load:

# In[75]:


server = Server()
server.add_connection("192.168.1.1")

# 로드 메서드 호출
print(server.load())


# After running the above code cell, if you get a **<font color =red>NameError</font>** message, be sure to run the Server class definition code block first.
# 
# The output should be 0.  This is because some things are missing from the Server class. So, you'll need to go back and fill in the blanks to make it behave properly. 
# <br><br>
# Go back to the Server class definition and fill in the missing parts for the `add_connection` and `load` methods to make the cell above print a number different than zero.  As the load is calculated randomly, this number should be different each time the code is executed.
# <br><br>
# **Hint:** Recall that you can iterate through the values of your connections dictionary just as you would any sequence.

# Great! If your output is a random number between 1 and 10, you have successfully coded the `add_connection` and `load` methods of the Server class.  Well done!
# <br><br>
# What about closing a connection? Right now the `close_connection` method doesn't do anything. Go back to the Server class definition and fill in the missing code for the `close_connection` method to make the following code work correctly:

# In[76]:


server.close_connection("192.168.1.1")

# 딕셔너리 요소 삭제 후, 로드 메서드 호출
print(server.load())


# You have successfully coded the `close_connection` method if the cell above prints 0.
# <br><br>
# **Hint:** Remember that `del` dictionary[key] removes the item with key *key* from the dictionary.

# Alright, we now have a basic implementation of the server class. Let's look at the basic LoadBalancing class. This class will start with only one server available. When a connection gets added, it will randomly select a server to serve that connection, and then pass on the connection to the server. The LoadBalancing class also needs to keep track of the ongoing connections to be able to close them. This is the basic structure:

# In[78]:


#Begin Portion 2
class LoadBalancing:
    
    def __init__(self):
        """Initialize the load balancing system with one server"""
        # 생성자 호출, Dict 타입과 List 타입의 멤버 변수 정의
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        # 부하분산하도록 서버에 랜덤하게 커넥션 할당하는 메서드
        
        # 리스트에 있는 서버 중 랜덤 선택
        server = random.choice(self.servers)
        
        # Add the connection to the dictionary with the selected server
        # LoadBalancing 클래스의 멤버 변수 connections에 key, val 추가
        # id가 key인 이유는 바로 아래 메서드에서 설명됨
        self.connections[connection_id] = server
        
        # Add the connection to the server
        # 멤버 변수 server는 Server 클래스의 객체이기 때문에 해당 클래스의 메서드 add_connection에 접근함
        server.add_connection(connection_id)
        
        # 커넥션 오버헤드 방지
        self.ensure_availability()


    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # 커넥션 id를 기준으로 서버를 찾고, 해당 서버의 커넥션을 제거하는 메서드
        
        # Find out the right server
        # 딕셔너리의 키 요소들 중 파라미터로 받은 id와 일치하는 것 탐색
        for connection in self.connections.keys():
            if connection == connection_id:
                
                # 일치하면 키에 해당하는 val(서버)를 임시 변수에 대입
                target_server = self.connections[connection]
                
                # Close the connection on the server
                # 임시 변수 target_server(= server)는 Server 클래스의 객체이기 때문에 해당 클래스의 메서드 close_connection에 접근함
                target_server.close_connection(connection_id)
        
        # Remove the connection from the load balancer
        del self.connections[connection_id]


    def avg_load(self):
        """Calculates the average load of all servers"""
        # 모든 서버 객체의 딕셔너리에 있는 로드 값 다 합쳐서 평균을 구하는 메서드
        
        # 모든 서버의 로드 값 합계
        result = 0
        # 서버 개수
        loads = 0
        
        # Sum the load of each server and divide by the amount of servers
        # 각 서버의 로드 값 합계를 구하고, 동시에 서버 개수를 카운팅함
        for server in self.servers:
            result += server.load()
            loads += 1
        
        # 서버들의 로드 값 평균
        return result/loads

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        # 서버들의 로드 값 평균이 50% 넘어가면 새로운 서버 객체를 생성하는 메서드
        
        # 평균 구하는 메서드 호출
        if self.avg_load() >= 50:
            
            # 리스트 servers에 새로운 객체를 요소로 추가
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        # 로드밸런싱 클래스 프린트하면 출력될 메세지
        # 멤버 변수 loads에 서버 객체들의 str 함수 호출하여 출력된 값으로 리스트 comprehesion
        loads = [str(server) for server in self.servers]
        
        # 리스트 loads의 요소들을 ,(콤마)와 함께 출력
        return "[{}]".format(",".join(loads))
    
#End Portion 2#


# As with the Server class, this class is currently incomplete. You need to fill in the gaps to make it work correctly. For example, this snippet should create a connection in the load balancer, assign it to a running server and then the load should be more than zero:

# In[79]:


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())


# After running the above code, the output is 0.  Fill in the missing parts for the `add_connection` and `avg_load` methods of the LoadBalancing class to make this print the right load. Be sure that the load balancer now has an average load more than 0 before proceeding.

# What if we add a new server?

# In[80]:


l.servers.append(Server())

# 서버 2개 됐으니까 위 값의 절반 값이 나와야 함
print(l.avg_load())


# The average load should now be half of what it was before. If it's not, make sure you correctly fill in the missing gaps for the `add_connection` and `avg_load` methods so that this code works correctly. 
# <br><br>
# **Hint:** You can iterate through the all servers in the *self.servers* list to get the total server load amount and then divide by the length of the *self.servers* list to compute the average load amount.

# Fantastic! Now what about closing the connection?

# In[81]:


l.close_connection("fdca:83d2::f20d")

# 커넥션 하나 있던 서버 제거함 -> 서버는 여전히 2대이지만, 커넥션 Zero
print(l.avg_load())


# Fill in the code of the LoadBalancing class to make the load go back to zero once the connection is closed.
# <br><br>
# Great job! Before, we added a server manually. But we want this to happen automatically when the average load is more than 50%. To make this possible, fill in the missing code for the `ensure_availability` method and call it from the `add_connection` method after a connection has been added. You can test it with the following code:

# In[82]:


for connection in range(20):
    l.add_connection(connection)

# 2개의 서버에 20개의 커넥션 할당했더니, 평균 로드 값이 50% 넘어서 3번 째 서버 객체 생성함
print(l)


# The code above adds 20 new connections and then prints the loads for each server in the load balancer.  If you coded correctly, new servers should have been added automatically to ensure that the average load of all servers is not more than 50%.
# <br><br>
# Run the following code to verify that the average load of the load balancer is not more than 50%.

# In[83]:


print(l.avg_load())
# 서버가 3개가 되면서 평균 값이 다시 낮아짐


# Awesome! If the average load is indeed less than 50%, you are all done with this assessment.
