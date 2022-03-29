
/*
Bubble Sort
The bubble sort method starts at the beginning of an unsorted array and 'bubbles up' unsorted values towards the end,
iterating through the array until it is completely sorted.
It does this by comparing adjacent items and swapping them if they are out of order.
The method continues looping through the array until no swaps occur at which point the array is sorted.
*/
function bubbleSort(array) {
    // Only change code below this line
    for (let i = 0; i < array.length; i++) {
        if (array[i+1] < array[i]) {
            for (let position = i+1; position > 0; position--) {
                if (array[position] < array[position-1]) {
                    let temp = array[position-1];
                    array[position-1] = array[position];
                    array[position] = temp;
                }
                else {
                    break;
                }
            }
        }
    }
    return array;
    // Only change code above this line
  }


  /*
Selection sort works by selecting the minimum value in a list and swapping it with the first value in the list.
It then starts at the second position, selects the smallest value in the remaining list,
and swaps it with the second element.
It continues iterating through the list and swapping elements until it reaches the end of the list.
Now the list is sorted. Selection sort has quadratic time complexity in all cases
  */
function selectionSort(array) {
    // Only change code below this line
    for (let i = 0; i < array.length; i++) {
        // Find Minimum
        let minimumPosition = i;
        let minimum = array[i];
        for (let j = i+1; j < array.length; j++) {
            if (array[j] < minimum) {
                minimumPosition = j;
                minimum = array[j];
            }
        }
        array = array.slice(minimumPosition);
        array.splice(i, 0, minimum);
    }
    return array;
    // Only change code above this line
  }

// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-selection-sort