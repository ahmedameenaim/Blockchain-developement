const SHA256 = require('crypto-js/SHA265');

class Block {
    constructor(index, prevhash ,timestamp, data){
        this.index = index ;
        this.prevhash = prevhash ;
        this.timestamp = timestamp ;
        this.data = data;
        this.hash = this.calcHash(index, prevhash, timestamp, data) ;
    }
    Let Blockchain = [gensisBlock];
    
    const getlastestBlock = () => Blockchain[Blockchain.length - 1];

    calcHash(index, prevhash, timestamp, data) {
        return SHA256(index + prevhash + timestamp + data + hash).toString();
    }
}

const calcBlockhash = (Block) => {
    return SHA256(Block.index + Block.prevhash + Block.timestamp + Block.data + Block.hash).toString();
}

const CreateNewBlock = (data) => {
    const prevBlock = getlastestBlock();
    const index = prevBlock.index + 1 ;
    const prevHash = prevBlock.hash ;
    const timestamp = new Date.().getTime();
    return new Block(index, prevhash, timestamp, data);
}

const isBlockValid = (Block) => {
    return typeof Block.index === 'number' &&
        typeof Block.prevhash === 'string' &&
        typeof Block.timestamp === 'number' &&
        typeof Block.data === 'string' &&
        typeof Block.hash === 'string' && ;

const isBlockValid = (prevBlock, Block) => {
    if(!isBlockValid(prevBlock) && !isBlockValid( Block)) {
        return false ;
    }else if (prevBlock.index === Block.index - 1) {
        if (prevBlock.hash === Block.prevHash){
            if (calcBlockHash(Block) === Block.hash){
                return true;
            }


        }
    }
}        


}
const AddBlock = (Block) => {

}

const gensisBlock = new Block(0,'', 1234567890, 'GBlock')

console.log(gensisBlock);