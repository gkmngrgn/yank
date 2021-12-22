package main

import (
	"fmt"
	"net"
	"os"
)

const (
	CONN_HOST = "0.0.0.0"
	CONN_PORT = "3000"
	CONN_TYPE = "tcp"
)

func main() {
	l, err := net.Listen(CONN_TYPE, CONN_HOST+":"+CONN_PORT)
	if err != nil {
		fmt.Println("ERROR LISTENING: ", err.Error())
		os.Exit(1)
	}

	defer l.Close()

	fmt.Println("Server started: " + CONN_HOST + ":" + CONN_PORT)

	for {
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("ERROR ACCEPTING: ", err.Error())
			os.Exit(1)
		}

		go handleRequest(conn)
	}
}

func handleRequest(conn net.Conn) {
	buf := make([]byte, 1024)

	size, err := conn.Read(buf)
	if err != nil {
		fmt.Println("ERROR READING: ", err.Error())
	}

	msg := fmt.Sprintf("Message received: %s", buf[:int(size)])

	conn.Write([]byte(msg))
	conn.Close()
}
