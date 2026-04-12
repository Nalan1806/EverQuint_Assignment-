function trapwater(heights){
    let n =heights.length;
    let leftMax=new Array(n).fill(0);
    let rightMax=new Array(n).fill(0);
    let water=new Array(n).fill(0);

    //for finding leftMax
    leftMax[0] = heights[0];
    for(let i=1;i<n;i++){
        leftMax[i] = Math.max(leftMax[i-1],heights[i]);
    }

    //for finding rightMax
    rightMax[n-1] = heights[n-1];
    for(let i=n-2;i>=0;i--){
        rightMax[i]=Math.max(rightMax[i+1],heights[i]);

    }

    //water calculation

    for(let i=0;i<n;i++){
        water[i]=Math.max(0,Math.min(leftMax[i],rightMax[i])-heights[i]);
        
    }
    //total water
    let total=0;
    for(let w of water){
        total+=w;
    }

    return{
        total:total,
        water:water
    };



}



//input parsing 
function parseInput(input){
         return input
        .replace(/\[|\]/g, "")
        .split(",")
        .map(x => Number(x.trim()));
}

//buttonhandler for connecting ui -> logic
function handleCompute(){
    let input = document.getElementById("inputArray").value;
    let heights=parseInput(input);
    let result = trapwater(heights);

    document.getElementById("output").innerText = "Total Water: " + result.total; 
}