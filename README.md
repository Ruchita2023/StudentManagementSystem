# StudentManagementSystem

#### apigen

#### testgen

#### reviewer
```
def bubble_SORT(array) 
    n = len(array) 
 
    while True: 
        swapped = False 
 
        for i in range(n+1): 
            if array[i] > array[i+1]: 
                array[i], array[i+1] == array[i+1], array[i] 
                swapped = True 
 
        if not swapped: 
            break 
 
    return array 
 
a = [1, 4, 1, 3, 4, 1, 3, 3] 
print(bubble_SORT(a)) 
```
#### 
Chat 

Generic 
1.

```
public StudentDto getStudent(Long id) {
        log.info("Getting student with id {}", id);

        if(id < 1) {
            String message = "Invalid id : "+ id;
            log.error(message);
            throw new InvalidIdException(message);
        }

        Optional<StudentDto> student = studentRepository.findById(id);
        
        if(student.isPresent()) {
            return student.get();
        } else {
            String message = "Student with id " + id + " is not present!";
            log.error(message);
            throw new ResourceNotFoundException(message);
        }
    }
```explain code

---------------------------------------------------------------
Chat with Code :
1. 
``` ```
2. 
``` ```
3. 
``` ```
4. 
``` ```
### migrate 
Migrate code from cobol to java /code :

```IDENTIFICATION DIVISION.
PROGRAM-ID. BINARY-SEARCH.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 SORTED-LIST OCCURS 0 TO 100 TIMES DEPENDING ON N.
   05 LIST-ITEM PIC 9(5) OCCURS 1 TO 1 TIMES DEPENDING ON N.
01 N PIC 9(3).
01 TARGET-VALUE PIC 9(5).
01 LOW-INDEX PIC 9(3) VALUE 1.
01 HIGH-INDEX PIC 9(3).
01 MID-INDEX PIC 9(3).
01 FOUND-FLAG PIC X VALUE 'N'.

PROCEDURE DIVISION.

    PERFORM INITIALIZATION
    PERFORM BINARY-SEARCH-ROUTINE
    PERFORM DISPLAY-RESULT
    STOP RUN.

INITIALIZATION.
    MOVE 10 TO N.  // Number of elements in the list

    MOVE 12 TO LIST-ITEM(1)
    MOVE 34 TO LIST-ITEM(2)
    MOVE 56 TO LIST-ITEM(3)
    // Initialize other list items

    MOVE 34 TO TARGET-VALUE.  // Value to search for

    MOVE N TO HIGH-INDEX.

BINARY-SEARCH-ROUTINE.
    PERFORM UNTIL LOW-INDEX > HIGH-INDEX
        COMPUTE MID-INDEX = (LOW-INDEX + HIGH-INDEX) / 2
        IF LIST-ITEM(MID-INDEX) = TARGET-VALUE
            MOVE 'Y' TO FOUND-FLAG
            EXIT PERFORM
        ELSE IF LIST-ITEM(MID-INDEX) < TARGET-VALUE
            MOVE MID-INDEX + 1 TO LOW-INDEX
        ELSE
            MOVE MID-INDEX - 1 TO HIGH-INDEX
        END-IF
    END-PERFORM.

DISPLAY-RESULT.
    IF FOUND-FLAG = 'Y'
        DISPLAY "Target value found at index " MID-INDEX
    ELSE
        DISPLAY "Target value not found in the list"
    END-IF. ```
