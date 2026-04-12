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
    drawVisualization(heights,result.water); 
}



function drawVisualization(heights,water){
    let svg=document.getElementById("visualization");

    svg.innerHTML=""; //this is for clearing previous drawing
    let barWidth=40;
    let scale=20; //for scale factor so that height is visible 

    //simple y-axis label
    for(let i=0;i<=10;i++){
        let y = 300 - i*scale;

        let text = document.createElementNS("http://www.w3.org/2000/svg", "text")
        text.setAttribute("x", 0);
        text.setAttribute("y", y);
        text.setAttribute("font-size", "10");
        text.setAttribute("fill", "gray");

        text.textContent = i;
        svg.appendChild(text);
    }

    
   

    for(let i=0;i<heights.length;i++){
        let x=i*barWidth + 40; //we shift bars slightly right since we put axes

        //yellow height block
        let blockHeight=heights[i]*scale;
        let yBlock=300-blockHeight; //y position (SVG origin is top-left,so we subtract)
        let rectBlock=document.createElementNS(
            "http://www.w3.org/2000/svg", "rect"
        );

        rectBlock.setAttribute("x",x);
        rectBlock.setAttribute("y",yBlock);
        rectBlock.setAttribute("width",barWidth-5);
        rectBlock.setAttribute("height",blockHeight);

        //for settign color
        rectBlock.setAttribute("fill","gold")

        
        svg.appendChild(rectBlock) //add to SVG


        //blue water

        let waterHeight=water[i]*scale;
        let yWater=yBlock-waterHeight;

        let rectWater=document.createElementNS(
            "http://www.w3.org/2000/svg", "rect"
        ); //create the water rectangle

        //set position and size
        rectWater.setAttribute("x",x);
        rectWater.setAttribute("y",yWater);
        rectWater.setAttribute("width",barWidth-5);
        rectWater.setAttribute("height",waterHeight);

        rectWater.setAttribute("fill","skyblue");

        //add to SVG
        svg.appendChild(rectWater);
         

    }
        

    }
