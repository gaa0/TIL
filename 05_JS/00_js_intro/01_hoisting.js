//hoisting!
// 나중에 선언된 변수를 참조 할 수 있음
// 함수 or statement 최상단으로 올려지는것(hosting)
// 변수와 함수를 위한 메모리를 확보하는 과정

// console.log(a)
// var a = 10
// console.log(a)

/*
// let b = 10
// console.log(b)


console.log(a)
var a = 10
console.log(a)
//var가 호이스트 되는 과정
//1. 선언이 최상단으로 올라감
var a
//2. 선언이 최상단으로 올라갔기 때문에 에러가 나지 않고
// undefind가 출력
// (TMI) JS에서는 var 변수를 선언할 때 값을 넣어주지않으면 undefind를
//자동으로 넣어줌
console.log(a)
// 할당은 그 위에 이루어짐
console.log(a)


//let
console.log(b)
let b = 10
console.log(b)

/// let이 호이스트 되는 과정
//1. 선언이 최상단으로 
let b
//2. 근데 에러??
console.log(b)
//3. 할당
b = 10
//4. 출력 
console.log(b)

// var 할당 과정
//1. 선언 - 초기화 (동시에 진행) -> 처음에는 값이 없기 때문에 js 가 undefined를 할당
// let 할당 진행

//let 할당 과정
//1. 선언 -> 초기화 x
//2. TDZ(Temperal Dead Zone) -> 임시적 사각지대
//3. 초기화(초기에는 값이 없기 때문에 undefined 를 할당)
//4. 할당


let foo 
let bar = undefined

console.log(foo)
console.log(bar)


x
let x = 1


y
var y =1 
console.log(y)

var y //1.선언이 끌어올려진다. 이때 초기화가 같이 이루어지고 값이 없어서 undefined를 넣어준다.
y = 1 //2. 값이 할당된다.
console.log(y) //3. 값이 출력된다ㅣ

if (x !== 1) {
  console.log(y)
  var y = 3
  if (y==3) {
    var x = 1
  }
  console.log(y)
}

if (x ==1 ) {
  console.log(y)
}

x = 7
console.log(x)

*/


