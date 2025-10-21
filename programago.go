package main

import (
	"bufio"
	"fmt"
	"go.bug.st/serial"
)

func main() {
	port, err := serial.Open("COM3", &serial.Mode{BaudRate: 115200})
	if err != nil {
		panic(err)
	}
	defer port.Close()

	fmt.Println("Conectado al micro:bit")

	scanner := bufio.NewScanner(port)
	for scanner.Scan() {
		fmt.Println("Dato recibido:", scanner.Text())
	}
}
