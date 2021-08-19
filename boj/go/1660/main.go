package main

import (
	"bufio"
	"fmt"
	"os"
)

var dp [300001]int

func main() {
	r := bufio.NewReader(os.Stdin)
	var n int // input
	fmt.Fscan(r, &n)

	tetra := []int{}

	for i := 1; true; i++ {
		val := i * (i + 1) * (i + 2) / 6
		if val > n {
			break
		}
		tetra = append(tetra, val)
	}

	for i := 0; i <= n; i++ {
		dp[i] = 300000
	}

	for i := 0; i < len(tetra); i++ {
		dp[tetra[i]] = 1
	}

	for i := 0; i < len(tetra); i++ {
		for j := tetra[i]; j <= n; j++ {
			// fmt.Println(j - tetra[i])
			fromMemo := dp[j-tetra[i]] + 1
			if dp[j] > fromMemo {
				dp[j] = fromMemo
			}
		}
	}

	// fmt.Println(tetra)
	fmt.Println(dp[n])
}
