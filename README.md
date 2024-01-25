# Stock Management Simulator with RPC

## Introduction to RPC as a Middleware Service

Remote Procedure Call (RPC) is a middleware service that facilitates communication between distributed systems by allowing one program to invoke procedures in another address space, typically on a remote machine. RPC abstracts the complexities of inter-process communication, making it appear as if functions are being called locally.

## Project Overview

In this project, we demonstrate the use of RPC in a Stock Management Simulator. The objective is to showcase how RPC can be employed to manage stock-related operations such as buying, selling, and checking stock prices within a distributed system.

## Implementing RPC in Stock Management Simulator

### Architecture of RPC Middleware Service

The project is structured into server and client components, leveraging Python's `xmlrpc` library for RPC communication. The server exposes methods for handling stock-related actions, while the client remotely invokes these methods.

```plaintext
stock_management_simulator/
|-- server/
|   |-- __init__.py
|   |-- stock_server.py
|
|-- client/
|   |-- __init__.py
|   |-- stock_client.py
|
|-- common/
|   |-- __init__.py
|   |-- stock_data.py
|
|-- venv/
|-- requirements.txt
|-- README.md
```

### Operation of System

**1 - Server Operation:**
- The server initializes stock data and registers RPC methods (get_stock_prices, buy_stock, sell_stock).
- It listens on a specified port (e.g., 8000) to handle incoming RPC requests.

**2 - Client Operation:**
- The client connects to the server using RPC.
- It remotely calls the server's RPC methods to retrieve stock prices or perform buy/sell operations.


## Advantages of RPC over Other Middleware Services

**- Simplicity:**
RPC simplifies distributed communication by abstracting the complexities associated with remote procedure calls.

**- Language Agnostic:**
RPC facilitates communication between systems implemented in different programming languages.

**- Efficiency:**
RPC provides efficient communication, minimizing the overhead associated with remote procedure calls.

**- Interoperability:**
gRPC supports multiple programming languages, allowing components written in different languages to seamlessly communicate.


### Screenshots

**Directory Setup**
![directory setup](images/dir_setup.png "Directory Setup")

**Server Running**
![server running](images/server_running.gif "Server Running")

**Client Running**
![client running](images/client_running.gif "Client Running")

**Server Code Snippet**
![Server Codes](images/client_running.gif "Client Running")

**Client Code Snippet**
![Client Codes](images/client_running.gif "Client Running")


## Getting Started

**1. Set up a virtual environment:**
```
python -m venv venv
.\venv\Scripts\activate
```

**2. Install dependencies:**
```
pip install -r requirements.txt
```

**3. Run the server and client programs separately to see how they communicate.**
```
cd server
python stock_server.py
```

```
cd client
python stock_client.py
```