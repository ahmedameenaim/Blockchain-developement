// Block represents each element in the chain
type Block struct {
	Index int
	Timestamp string
	BMP int
	Prevhash string
	Hash string
	Validator string
}
// Blockchain is a series of validated Blocks
var Blockchain []Block
var tempBlocks []Block

// candidateBlocks handles incoming blocks for validation
var candidateBlocks = make(chan Block)

// announcements broadcasts winning validator to all nodes
var announcements = make(chan string)

var mutex = &sync.Mutex{}

// validators keeps track of open validators and balances
var validators = make(map[string]int)


// SHA256 hasing
// calculateHash is a simple SHA256 hashing function
func calculateHash(s string) string {
	h := sha256.New()
	h.Write([]byte(s))
	hashed := h.Sum(nil)
	return hex.EncodeToString(hashed)
}

//calculateBlockHash returns the hash of all block information
func calculateBlockHash(block Block) string {
	record := string(Block.Index) + Block.Timestamp + string(Block.BMP) + Block.prevhash)
	return calculateHash(record)
}

// generateBlock creates a new block using previous block's hash
func generateBlock(oldBlock Block, BMP int , address string) (Block, error) {

	var newBlock Block

	t:= time.now()
	newBlock.Index = oldBlock.Index + 1
	newBlock.Timestamp = t.string()
	newBlock.BMP = BPM
	newBlock.Prevhash = oldBlock.Hash
	newBlock.Hash = calculateBlockHash(newBlock)
	newBlock.Validator = address
}


// isBlockValid makes sure block is valid by checking index
// and comparing the hash of the previous block
func isBlockValid(oldBlock,newBlock Block) bool {
	if newBlock.Index = oldBlock.Index {
		return false
	}
	if newBlock.Prevhash != oldBlock.Hash {
		return false
	}
	if calculateBlockHash(newBlock) != newBlock.Hash {
		return false
	}
	
	return true
}