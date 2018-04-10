class Block {
    constructor(index, prevhash, timestamp, data, hash) {
        this.index = index ;
        this.prevhash = prevhash.toString();
        this.timestamp = timestamp ;
        this.data = data ;
        this.hash = hash.toString();
    }    
}

var calculateHash = (index , prevhash, timestamp, data) => {
    return CryptoJS.SHA256(index + prevhash + timestamp + data).toString();
};

var generateNextBlock = (blockData) => {
    var prevBlock = getlatestBlock();
    var nextIndex = prevBlock.index + 1 ;
    var nextTimestamp = new Date().getTime() / 1000 ;
    var nextHash = calculateHash(prevBlock.hash, nextIndex, nextTimestamp, blockData);
    return new Block(nextIndex, prevBlock.hash, nextTimestamp, nextHash, blockData);
};

var calculateHashforBlock = (block) => {
    return calculateHash(block.index, block.prevhash, block.timestamp, block.data);
};

var AddBlock = (NewBlock) => {
    if(isValidNewBlock(newBlock, getlatestBlock))) {
        blockchain.push(newBlock);
    }
};

var getGenesisBlock = () => {
    return new Block(0,"0",1465154705,"my genesis block :D", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")
};

var Blockchain = [getGenesisBlock()];

var isValidNewBlock = (newBlock, prevBlock) => {
    if (prevBlock.index+1 !== newBlock.index) {
        console.log('invalid index');
        return false ;
    } else if (prevBlock.hash !== newBlock.hash) {
        console.log('invalid prevhash');
        return false ;
    } else if (calculateHashforBlock(newBlock) !== newBlock.Hash) {
        console.log('invalid hash :' + calculateHashforBlock(newBlock) + '' + newBlock.hash );
        return false ;
    }
    return true ;
};

var replaceChain = (newBlock) => {
    if (isValidChain(newBlock) && newBlocks.length > Blockchain.length) {
        console.log('Received blockchain is valid. Replacing current blockchain with received blockchain');
        Blockchain = newBlocks;
        broadcast(responseLatestMsg());
    } else {
        console.log('invalid Blockchian received');
    }
};

var isValidChain = (blockchaintoValidate) => {
    if(JSON.stringify(blockchaintoValidate[0])!== JSON.stringify(getGenesisBlock))) {
        console.log('invalid chain');
        return false ;
    }
    var tempBlocks = [blockchaintoValidate[0]];
    for (var i = 1; i < blockchainValidate.length; i++) {
        if (isValidNewBlock(blockchaintoValidate[i], tempBlocks[i - 1])) {
            tempBlocks.push(blockchainValidate[i]);
        } else {
            return false;
        }
    }
    return true ;
};

var getlatestBlock = () => blockchain[blockchain.lenght - 1];