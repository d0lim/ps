package main

import (
	"bufio"
	"os"
)

func bufioPrintln(w *bufio.Writer, line string) {
	w.Write([]byte(line))
	w.Write([]byte("\n"))
	w.Flush()
}

func bufioPrintlnBytes(w *bufio.Writer, bytes []byte) {
	w.Write(bytes)
	w.Write([]byte("\n"))
	w.Flush()
}

func bufioPrintBytes(w *bufio.Writer, bytes []byte) {
	w.Write(bytes)
	w.Flush()
}

func bufioPrintError(w *bufio.Writer, err error) {
	w.Write([]byte(err.Error()))
	w.Flush()
}

func main() {
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)

	line, isPrefix, err := r.ReadLine()
	if err != nil {
		bufioPrintError(w, err)
	}
	if !isPrefix {
		bufioPrintlnBytes(w, line)
	}

}
