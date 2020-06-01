package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	for {
		input := [51][51]int{}
		var w int
		var h int
		fmt.Fscan(r, &w, &h)
		// fmt.Println("w, h is", w, h)
		// fmt.Printf("%T\n", w)
		// fmt.Printf("%T\n", h)

		for i := 0; i < w; i++ {
			for j := 0; j < h; j++ {
				fmt.Fscan(r, &input[i][j])
			}
		}

		for i := 0; i < w; i++ {
			for j := 0; j < h; j++ {
				fmt.Printf("%d ", input[i][j])
			}
			fmt.Println()
		}

	}

}
