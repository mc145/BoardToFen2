let pieceClassifier; 
let resultText; 


const modelNumber = 6; 

let photo; 
function preload(){
    photo = loadImage('testing/data/photo.png'); 
}

function setup(){
    createCanvas(400,400);
    image(photo, 0, 0); 



    let options = {
        inputs: [64,64,4],
        task: 'imageClassification',
        debug: true
    }; 

    pieceClassifier = ml5.neuralNetwork(options); 
    const modelDetails = {
        model: `model1.0.${modelNumber}/model.json`,
        metadata: `model1.0.${modelNumber}/model_meta.json`,
        weights: `model1.0.${modelNumber}/model.weights.bin`
    }; 
    pieceClassifier.load(modelDetails, modelLoaded); 
    resultText = createDiv('loading model'); 
}


function modelLoaded(){
    console.log("MODEL HAS BEEN LOADED!"); 
}


function mousePressed(){

pieceClassifier.classify({ image: photo }, gotResults); 
}



function gotResults(err, result){
    if(err){
        console.log(err);
        return; 
    }
    console.log(result[0].label, `${result[0].confidence*100}%`); 
    resultText.html(`${result[0].label} ${result[0].confidence * 100}%`); 
   
}




function draw(){
    image(photo, 0, 0, width, height); 
}
