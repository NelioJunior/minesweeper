'use strict';

var components = {
    num_of_rows : 12,
    num_of_cols : 24,
    num_of_bombs : 55,
    bomb : '💣',
    alive : true,
    colors : {1: 'blue', 2: 'green', 3: 'red', 4: 'purple', 5: 'maroon', 6: 'turquoise', 7: 'black', 8: 'grey'}
}

function startGame() {

    while (field.lastElementChild) {
        field.removeChild(field.lastElementChild);
    }

    let url = './placeBombs?bombs=' + components.num_of_bombs + '&rows='+components.num_of_rows + '&cols='+components.num_of_cols;  

    fetch(url)
      .then((response) => {
        return response.json();
      })
      .then((jsonResp) => {
           components.bombs = jsonResp ;
           field.appendChild(createTable());    
      });
}

function cellID(i, j) {
    return 'cell-' + i + '-' + j;
}

function createTable() {
    var table, row, td, i, j;
    table = document.createElement('table');
    
    for (i=0; i<components.num_of_rows; i++) {
        row = document.createElement('tr');
        for (j=0; j<components.num_of_cols; j++) {
            td = document.createElement('td');
            td.id = cellID(i, j);
            row.appendChild(td);
            addCellListeners(td, i, j);
        }
        table.appendChild(row);
    }
    return table;
}

function addCellListeners(td, i, j) {
    td.addEventListener('mousedown', function(event) {
        if (!components.alive) {
            return;
        }
        components.mousewhiches += event.which;
        if (event.which === 3) {
            return;
        }
        if (this.flagged) {
            return;
        }
        this.style.backgroundColor = 'lightGrey';
    });

    td.addEventListener('mouseup', function(event) {
      
        if (!components.alive) {
            return;
        }

        if (this.clicked && components.mousewhiches == 4) {
            performMassClick(this, i, j);
        }

        components.mousewhiches = 0;
        
        if (event.which === 3) {
           
            if (this.clicked) {
                return;
            }
            if (this.flagged) {
                this.flagged = false;
                this.textContent = '';
            } else {
                this.flagged = true;
                this.textContent = components.flag;
            }

            event.preventDefault();
            event.stopPropagation();
          
            return false;
        } 
        else {
            handleCellClick(this, i, j);
        }
    });

    td.oncontextmenu = function() { 
        return false; 
    };
}

function handleCellClick(cell, i, j) {

    if (!components.alive) {
        return;
    }

    if (cell.flagged) {
        return;
    }

    cell.clicked = true;

    if (components.bombs[i][j]) {
        cell.style.color = 'red';
        cell.textContent = components.bomb;
        gameOver();
        
    } else {
        cell.style.backgroundColor = 'lightGrey';
        let num_of_bombs = adjacentBombs(i, j);
        if (num_of_bombs) {
            cell.style.color = components.colors[num_of_bombs];
            cell.textContent = num_of_bombs;
        } 
        else {
            clickAdjacentBombs(i, j);
        }
    }
}

function adjacentBombs(row, col) {
    var i, j, num_of_bombs;
    num_of_bombs = 0;

    for (i=-1; i<2; i++) {
        for (j=-1; j<2; j++) {
            if (components.bombs[row + i] && components.bombs[row + i][col + j]) {
                num_of_bombs++;
            }
        }
    }
    return num_of_bombs;
}

function adjacentFlags(row, col) {
    var i, j, num_flags;
    num_flags = 0;

    for (i=-1; i<2; i++) {
        for (j=-1; j<2; j++) {
            cell = document.getElementById(cellID(row + i, col + j));
            if (!!cell && cell.flagged) {
                num_flags++;
            }
        }
    }
    return num_flags;
}

function clickAdjacentBombs(row, col) {
    var i, j, cell;
    
    for (i=-1; i<2; i++) {
        for (j=-1; j<2; j++) {
            if (i === 0 && j === 0) {
                continue;
            }
            cell = document.getElementById(cellID(row + i, col + j));
            if (!!cell && !cell.clicked && !cell.flagged) {
                handleCellClick(cell, row + i, col + j);
            }
        }
    }
}

function performMassClick(cell, row, col) {
    if (adjacentFlags(row, col) === adjacentBombs(row, col)) {
        clickAdjacentBombs(row, col);
    }
}

function gameOver() {
    components.alive = false;
    document.getElementById('lost').style.display="block";
    
}

function reload(){
    window.location.reload();
}

window.addEventListener('load', function() {
    document.getElementById('lost').style.display="none";    
    startGame();

    btnSettings.onclick = () => {
        let rowsNumber = prompt("Please enter number of rows", 12);
        if (rowsNumber == NaN) {
            alert("Enter with a valid number");
            return; 
        } else if (rowsNumber == null) {
            return;             
        }

        let columsNumber = prompt("Please enter number of columns", 24);
        if (columsNumber == NaN) {
            alert("Enter with a valid number");
            return; 
        } else if (columsNumber == null) {
            return;             
        }

        let bombsNumber = prompt("Please enter number of mines", 55);
        if (bombsNumber == NaN) {
            alert("Enter with a valid number");
            return; 
        } else if (bombsNumber == null) {
            return;             
        }

        components = {
            num_of_rows : parseInt(rowsNumber) ,
            num_of_cols : parseInt(columsNumber) ,
            num_of_bombs : parseInt(bombsNumber) ,
            bomb : '💣',
            alive : true,
            colors : {1: 'blue', 2: 'green', 3: 'red', 4: 'purple', 5: 'maroon', 6: 'turquoise', 7: 'black', 8: 'grey'}
        }

        startGame();
    }

    btnAdd.onclick = (e) => {
        let first = 10;
        let second = 20;       
        let url = './add?a='+first+'&b='+second ;  

        fetch(url)
          .then((response) => {
            return response.json();
          })
          .then((myJson) => {
               alert("When I sun "+first+" and "+second+" I get: " + myJson.result);
          });

    }    
});