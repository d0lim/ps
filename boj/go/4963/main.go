package main

import (
	"bufio"
	"fmt"
	"os"
)

type (
	Stack struct {
		top    *node
		length int
	}
	node struct {
		value interface{}
		prev  *node
	}
)

// Create a new stack
func New() *Stack {
	return &Stack{nil, 0}
}

// Return the number of items in the stack
func (this *Stack) Len() int {
	return this.length
}

// View the top item on the stack
func (this *Stack) Peek() interface{} {
	if this.length == 0 {
		return nil
	}
	return this.top.value
}

// Pop the top item of the stack and return it
func (this *Stack) Pop() interface{} {
	if this.length == 0 {
		return nil
	}

	n := this.top
	this.top = n.prev
	this.length--
	return n.value
}

// Push a value onto the top of the stack
func (this *Stack) Push(value interface{}) {
	n := &node{value, this.top}
	this.top = n
	this.length++
}

// Coord is struct to express coordinate
type Coord struct {
	x int
	y int
}

var input [51][51]int

// var visit [51][51]int
var numberOfIsland int
var around [8]Coord

func dfs(x, y int) {
	// fmt.Println("Started dfs from", x, y)
	// s is the stack of coordinates
	s := New()
	s.Push(Coord{x, y})
	// 0 means visited, 1 means not visited
	if input[x][y] == 1 {
		// fmt.Println("Visited", x, y)
		input[x][y] = 0
		numberOfIsland++
		for s.Len() != 0 {
			// Get the coordinate of top of stack
			// with type assertion
			c := s.Pop().(Coord)
			x = c.x
			y = c.y

			// Check around the coordinate
			for i := 0; i < 8; i++ {
				nx := x + around[i].x
				ny := y + around[i].y
				// fmt.Println("Current nx:", nx, "ny:", ny)
				// Avoiding array out of bound exception
				if 0 <= nx && nx < 51 && 0 <= ny && ny < 51 {
					// and if we didn't reached this land then visit
					if input[nx][ny] == 1 {
						// fmt.Println("Visited", nx, ny)
						input[nx][ny] = 0

						// Push current x, y and nx, ny
						s.Push(Coord{x, y})
						s.Push(Coord{nx, ny})
					}
				}

			}
		}
	}

}

func main() {
	r := bufio.NewReader(os.Stdin)
	around = [8]Coord{
		{-1, -1},
		{0, -1},
		{1, -1},
		{-1, 0},
		{1, 0},
		{-1, 1},
		{0, 1},
		{1, 1},
	}
	for {
		// Initialize input and visit
		input = [51][51]int{}
		numberOfIsland = 0
		var w int
		var h int
		fmt.Fscan(r, &w, &h)
		// fmt.Println("w, h is", w, h)
		// fmt.Printf("%T\n", w)
		// fmt.Printf("%T\n", h)

		if w == 0 && h == 0 {
			break
		}

		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				fmt.Fscan(r, &input[i][j])
			}
		}
		// for i := 0; i < h; i++ {
		// 	for j := 0; j < w; j++ {
		// 		fmt.Printf("%d ", input[i][j])
		// 	}
		// 	fmt.Println()
		// }

		// DFS

		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				dfs(i, j)
			}

		}
		fmt.Println(numberOfIsland)
	}

}
