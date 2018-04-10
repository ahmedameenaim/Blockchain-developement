package main

import (
	"crypto/sha256"
	"time"
	"fmt"
)

type block struct {
	Timestamp int64
	Data []byte
	PrevBlockHash []byte
	Hash []byte
}

func (b *Block) SetHash() {
	timestamp := []byte(strconv.ForamtInt(b.Timestamp, 10))
	headers := bytes.join([][]byte{b.PrevBlockHash , b.Data, b.Timestamp}, byte{})
	hash := sha256.sum256(headers)
}

func NewBlock(data string , PrevBlockHash []byte) *Block {
	block := &Block{time.Now().Unix(), []byte(data), prevBlockHash, []byte{}}
	block.SetHash()
	return Block
}

type Blockchain struct {
	blocks []*Block
}

func (bc *Blockchain) AddBlock(data string) {
	prevBlock := bc.blocks[len(bc.blocks)-1]
	newBlock := NewBlock(data, prevblock.Hash)
	bc.blocks := append(bc.blocks , newBlock)
}

func NewGensisBlock() *Block {
	return NewBlock("Gensis Block", []byte{})
}

func NewBlockchain() *Blockchain {
	return &Blockchain{[]*Block{NewGenesisBlock()}}
}

func main() {
	bc := NewBlockchain()

	bc.AddBlock("Send 1 BTC to  Ivan")
	bc.AddBlock("Send 2 more BTC to Ivan")

	for _, block := range bc.blocks {
		fmt.Printf("Prev. hash: %x\n", block.PrevBlockHash)
		fmt.Printf("Data: %s\n", block.Data)
		fmt.Printf("Hash: %x\n", block.Hash)
		fmt.Println()
	}
}

