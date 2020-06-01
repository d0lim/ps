package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	var w int
	var h int
	fmt.Fscan(r, &w, &h)
	fmt.Println("w, h is", w, h)
}
