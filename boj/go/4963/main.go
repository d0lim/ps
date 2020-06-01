package main

import (
	"bufio"
	"os"
)

func main() {
	w := bufio.NewWriter(os.Stdout)

	r := bufio.NewReader(os.Stdin)

	line, isPrefix, err := r.ReadLine()
	if err != nil {
		w.Write([]byte(err.Error()))
		w.Flush()
	}
	if !isPrefix {
		w.Write(line)
		w.Write([]byte("\n"))
		w.Flush()
	}
	w.Write([]byte("Haha\n"))
	w.Flush()

}
