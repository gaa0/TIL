/*
// primitive(원시)타입
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8 //10^8
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number
console.log(a,b,c,d,e,f,g)
*/
//string

const sentence1 = 'Ask and go to the blue' //single
const sentence2 = "Ask and go to the blue" //double
const sentence3 = `Ask and go to the blue` // backtick

console.log(sentence1, sentence2, sentence3)

//따옴표를 사용하면 줄바꿈 불가 --> 백틱 이용

/*
const word = "안녕
하세요"

console.log(word) // 에러남

//굳이 하고싶으면 \n 하기

const word = "안녕\n하세요"


//백틱사용 -> 줄바꿈 + 문자열 사이에 변수도 넣을 수 잇다 ( python -f'string)
// 단, 이스케이프 문자열은 사용할 수 없습니다.

const word1 = `안녕
하세요`
console.log(word1)

const age = 10
const message = `홍길동은 ${age}
세입니다.`
console.group(message)


const happy = 'Will you join us?'
const hacking = 'happy' + 'ing' +'!'
console.log(happy,hacking)
 




const truthy = true
const falsy = false

console.log(truthy,falsy)
console.log(typeof truthy)
console.log(typeof falsy)

// Empty value
// JS -> null, undefined

let first_name // JS 넣어줌
console.log(first_name)

let last_name = null //의도적으로 값이 없음을 명시함
console.log(last_name)



console.log(typeof null)
console.log(typeof undefined)

console.log(null == undefined) //동등 비교 연산자
console.log(null === undefined) //일치 연산자

console.log(!null) // true
console.log(!undefined) //true


//연산자

//할당 연산자
let c = 0

c += 10

console.log(c)

c -= 3 
console.log(c)

c++
console.log(c)

c-- 
console.log(c)


//비교 연산자
// 변수 앞에 var, let, const를 명시적으로 붙여주지 않으면 js 엔진이
// 자동으로 var를 붙여줌
console.log(3>2)
console.log(3<2)

console.log('A'<'B')
console.log('Z'<'a')
console.log('가'<'나')

// 동등 비교 연산자(==) 
// 느슨한 평가, 사용을 지양하자 

const a =1

const b = '1'

console.log(a == b) //자동으로 형변환하기때문에 참이아닌데도
console.log(a != b) // 참으로나오고 거짓이 나옴
console.log(a == Number(b))

//자동 형변환 예시
console.log(8 * null) // 0 널을 형변환 0으로 함
console.log("5" - 1) // 4(number)
console.log("5" + 1) // 51(string)
console.log("five" *2 ) // NAN


// 일치 연산자 (===)


const a =1
const b = '1'

console.log(a === b) //false
console.log(a !== b) //true



//논리연산자
//and
console.log(true && false) // false
console.log(true && true) // true

console.log(1 && 0 ) // 0
console.log(0 && 1 ) // 0
console.log(4 && 7) //


//or
console.log(false || true )// true
console.log(false || false) // false

console.log(1||0) //1
console.log(0||1) //1
console.log(4||7) //4


//not
console.log(!true) // false
console.log(!false) // true

*/

//삼항 연산자
//가장 앞의 boolean 값이 참이면 : 
//앞의 값이 반환되고 반대일 경우에는 : 뒤의 값이 반환

console.log(true ? 1 : 2)
console.log(false ? 1 : 2)
console.log('nyapy' ? 'nice': 'awesome') //nice

//삼항 연산의 결과를 변수에 할당 할 수 있다~!
const result = Math.PI >4? "YAP": "NO" //NO
console.log(result)