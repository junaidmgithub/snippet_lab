class ContinousValues {
    
    constructor(values) {
        this.currentValue = null;
        this.currentValueIndex = 0;
        this.values = values;
        this.valuesMaxIndex = this.values.length - 1;
    }

    getValue() {
        if (this.currentValueIndex == 0) {
            this.currentValue = this.values[this.currentValueIndex];
            this.currentValueIndex++;  
        } else {
            if (this.currentValueIndex <= this.valuesMaxIndex) {
                this.currentValue = this.values[this.currentValueIndex];
                this.currentValueIndex++; 
            } else {
                this.currentValueIndex = 0;
                this.currentValue = this.values[this.currentValueIndex];
                this.currentValueIndex++;
            }
        }
        return this.currentValue;
    }

}


let all_colours = ['#FB8072', '#80B1D3', '#ee9c00',
'#58D68D', '#6e8bce', '#A9F1DF', '#FFECD2',
'#A1C4FD', '#764BA2', '#FF61D2', '#BFF098',
'#4E65FF', '#A9F1DF', '#FFECD2', '#A1C4FD',
'#764BA2', '#a59971', '#2E3192', '#D4145A',
'#009245', '#662D8C', '#EE9CA7', '#614385',
'#02AABD', '#FF512F', '#FF5F6D', '#11998E',
'#C6EA8D', '#EA8D8D', '#D8B5FF', '#FF61D2',
'#BFF098', '#4E65FF']


function test(){

    let rc = new ContinousValues(values=all_colours);
    
    for (var i=0; i<60;i++){
        console.log(rc.getValue());
    }
}

test();
