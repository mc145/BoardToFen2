let bishop = []; 
let king = []; 
let knight = []; 
let pawn = []; 
let queen = []; 
let rook = []; 


function preload(){
    for(let i = 0; i<100; i++){
        bishop[i] = loadImage(`data/bishop/augmented_bishop_${i}.png`);
        king[i] = loadImage(`data/king/augmented_king_${i}.png`);
        knight[i] = loadImage(`data/knight/augmented_knight_${i}.png`);
        pawn[i] = loadImage(`data/pawn/augmented_pawn_${i}.png`);
        queen[i] = loadImage(`data/queen/augmented_queen_${i}.png`);
        rook[i] = loadImage(`data/rook/augmented_rook_${i}.png`);
    }
}

let pieceClassifier; 

function setup(){
    createCanvas(400,400); 

    let options = {
        inputs: [64,64,4],
        task: 'imageClassification',
        debug: true
    }; 

    pieceClassifier = ml5.neuralNetwork(options); 
 
    for(let i = 0; i<bishop.length; i++){
        pieceClassifier.addData({ image: bishop[i] }, { label: 'bishop' }); 
        pieceClassifier.addData({ image: king[i] }, { label: 'king' }); 
        pieceClassifier.addData({ image: knight[i] }, { label: 'knight' }); 
        pieceClassifier.addData({ image: pawn[i] }, { label: 'pawn' }); 
        pieceClassifier.addData({ image: queen[i] }, { label: 'queen' }); 
        pieceClassifier.addData({ image: rook[i] }, { label: 'rook' }); 

    }

    const trainingOptions = {
        epochs: 35,
        batchSize: 12
    }; 


    pieceClassifier.normalizeData(); 
    pieceClassifier.train(trainingOptions, trainingFinished); 
}


function trainingFinished(){
    console.log("TRAINING FINISHED!"); 
    pieceClassifier.save(); 
}


