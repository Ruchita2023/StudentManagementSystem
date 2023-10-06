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
```

Chat with Code :
1. 
``` ```
2. 
``` ```
3. 
``` ```
4. 
``` ```
