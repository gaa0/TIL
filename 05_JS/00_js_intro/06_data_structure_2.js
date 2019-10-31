/*
//Array Helper Method

//Helper -> 자주 사용하는 로직을 재활용 할 수 있ㅇ게 도와주는 친구

//ESS 등장 -> ES6부터 적용됨
//forEach, filter, find, map, every, some, reduce

//1. forEach
//forEach는 주어진 callback을 배열에있는 각 요소에 대해 오름차순으로 한번씩 실행

//ES5
var colors = ['red','blud','green']

for (var i = 0; i < colors.length; i++ ){
  console.log(colors[i])
}


//ES6 +

const COLORS = ['red','blud','green']

COLORS.forEach(function(color) {
  console.log(color)
})

//한줄로 표현
COLORS.forEach( color => console.log(color))

//forEach는 아무 것도 리턴하지 않습니다.
const result = COLORS.forEach(color => console.log(color))
console.log(result)



//forEach = Ex1.

//ES5

function handlePOST() {
  const posts = [
    {id:23, title:'Daily JS News' },
    {id:52, title:'Code Refactor City' },
    {id:105, title:'The Brightest Ruby' },
  ]

  for (let i = 0; i< posts.length; i++){
    console.log(posts[i])
    console.log(posts[i].id)
    console.log(posts[i].title)
  }
}

handlePOST()

//ES6

function handlePOST() {
  const posts = [
    {id:23, title:'Daily JS News' },
    {id:52, title:'Code Refactor City' },
    {id:105, title:'The Brightest Ruby' },
  ]

  posts.forEach(function(post){
    console.log(post)
    console.log(post.id)
    console.log(post.title)
  }
  )
}


//한줄로 표현

function handlePOST() {
  const posts = [
    {id:23, title:'Daily JS News' },
    {id:52, title:'Code Refactor City' },
    {id:105, title:'The Brightest Ruby' },
  ]

  posts.forEach( post => (console.log(post),console.log(post.id),console.log(post.title)))
}
handlePOST()



//forEach ex-2
const images = [
  { height : 10, width : 30},
  {height : 20, width : 90},
  {height : 54, width : 32}
]


const areas =[]

images.forEach(function(image){
  areas.push(image.height * image.width)
})
console.log(areas)


//map
//배열 내의 모든 요소에 대해 각각 주어진 함수를 호출한 결과를 모아 새로운 배열 리턴

//ESS
var numbers = [1,2,3]
var doublenumbers = []

for (var i = 0; i < numbers.length; i++ ) {
  doublenumbers.push(numbers[i] * 2)
}
console.log(doublenumbers)
console.log(numbers)


//ES6+
const NUMBERS = [1, 2, 3]

const DOUBLE_NUMBERS = NUMBERS.map(function(number) {
  return number * 2
})
console.log(DOUBLE_NUMBERS)




//map - Ex1
//숫자가 담긴 배열을 받아 각 숫자의 제곱근이 들어있는 새로운 배열 만들기
const numbers = [4, 9, 16]
const roots = numbers.map(Math.sqrt)
console.log(roots)



//map Ex2
// images 배열 내의 object 안에 있는 height 값을 heights 라는 상수에 담아보세요

const images = [
  { height : '34px', width : '39px'},
  { height : '54px', width : '19px'},
  { height : '83px', width : '75px'},
]

const heights = images.map(function(image){
  return image.height
})

console.log(heights)


//map Ex3
// distance/time -> 속도를 저장하는 speeds(배열)을 만들어보세요

const trips = [
  { distance : 34, time : 39},
  { distance : 54, time : 19},
  { distance : 83, time : 75},
]

const speeds = trips.map(function(trip){
  return trip.distance / trip.time
})

console.log(speeds)

//map Ex4

//다음 두 배열을 객체 형태로 결합한 comics라는 배열을 만들어 보자

const brands = ['Marvel','DC']
const movies = ['IronMan','Batman']

//x -> 현재 elem
//i -> 그 elem의 index
const comics = brands.map((x,i)=> ({ name:x, hero:movies[i]}))
console.log(comics)

//3. filter
//주어진 함수의 테스트를 통과하는 모든 요소를 모아서 새로운 배열로 반환하는 핼퍼 매서드

//ES5

var products = [  
{ name : 'cucumber', type : 'vetetable'},
{ name : 'banana', type : 'fruit'},
{ name : 'carrot', type : 'vegetable'},
{ name : 'apple', type : 'fruit'},
]

var fruitProducts = []

for (var i=0; i < products.length; i++) {
  if (products[i].type === 'fruit') {
    fruitProducts.push(products[i])
  }
}
console.log(products)
console.log(fruitProducts)


//ES6+

const PRODUCTS = [
  { name : 'cucumber', type : 'vetetable'},
  { name : 'banana', type : 'fruit'},
  { name : 'carrot', type : 'vegetable'},
  { name : 'apple', type : 'fruit'},
]

const FRUIT_PRODUCTS = PRODUCTS.filter(function(product) {
  return product.type == 'fruit'
})

console.log(FRUIT_PRODUCTS)
console.log(PRODUCTS)


//filter -Ex1,
// filter 핼퍼 메서드를 사용해서 numbers 배열 중 50보다 큰 값만 필터링해서
//filteredNumbers 라는 배열에 담아주세요

const numbers = [15, 25, 35, 45 , 55, 65, 75, 85, 95]

const filteredNumbers = numbers.filter(function(number){
  return number > 50
})

console.log(filteredNumbers)
//filter - Ex2.
//users 배열에서 admin 레벨이 true인 유저 object만 filteredUsers라는 배열에 담아서
//두번째 유저 이름을 출력해보세요
//juan 출력
const users = [
  {id:1, admin:false, name:'justin'},
  {id:2, admin:false, name:'harry'},
  {id:3, admin:true, name:'tak'},
  {id:4, admin:false, name:'jason'},
  {id:5, admin:true, name:'juan'},
]

const filteredUsers = users.filter(function(user) {
  return user.admin == true
})

console.log(filteredUsers)

console.log(filteredUsers[1].name)


//4.reduce
//배열의 각 요소에 주어진 reducer 함수를 실행하고, 하나의 결과값을 retrun 합니다.
// 배열 내에 숫자, 총합, 평균 계산 등에 활용합니다.(배열의 값을 하나로 줄이는 일)


//합계
const ssafyTests = [90, 90, 80, 77]
//total = 누적값
//x = 초기값(option 설정해도되고 안해도되고)
const sum = ssafyTests.reduce((total,x) => total += x, 0)
console.log(sum)

// 평균
const avg = ssafyTests.reduce((total,x)=> total + x, 0) / ssafyTests.length
console.log(avg)


// reduce - Ex1
// 배열 내 요소의 총합 구하기
const arr = [0, 1, 2, 3]
const totalSum = arr.reduce(function(acc,currentValue) {
  return acc + currentValue
}
console.log(totalSum)//6

// reduce -Ex2
//배열에 담긴 중복된 이름을 {'이름':수}의 object로 반환 하세요(심화)

const names = ['harry','jason','tak','tak','justin']

const countedNames = names.reduce(function(allNames,name) { 

  if (name in allNames) {
    allNames[name]++;

  }
  else {
    allNames[name] = 1
  }
  return allNames
},{})
console.log(countedNames)


//5. find
// 주어진 판별 함수를 만족하는 첫번째 요소 값을 반환, 값이 없다면 undefined를 반환
var users = [
  {name:'Tony stark', age:45},
  {name:'Steve Rogers', age:32},
  {name:'Thor', age:40},
  {name:'Tony stark', age:23},
]

for (var i = 0; i < users.length; i++) {
  if (users[i].name === 'Tony stark') {
    var user = users[i]
    break
  }
}

console.log(user)


//ES6+
const USERS = [
  {name:'Tony stark', age:45},
  {name:'Steve Rogers', age:32},
  {name:'Thor', age:40},
  {name:'Tony stark', age:23},
]
//길게적어보귀
const user = USERS.find(function(user){
  return user.name == 'Tony stark'
})

// 화살표 문법으로 리팩토링
const user = USERS.find( user => user.name == 'Tony stark')

console.log(user)

//6. some & every

//some과 every는 대상 배열에서 특정 요소를 뽑거나, 배열을 return하지 않고
//조건에 대해 boolean을 return

//some
//배열 내의 어던 요소라소(==하나라도) 주어진 함수를 통과하는지 테스트하고 결과에 따라 boolean return
const arr = [1, 2, 3, 4, 5]
const result = arr.some( elem => elem %2 ===0 )
console.log(result)
//every
//배열 내의 모든 요소가 주어진 함수를 통과하는지 테스트하고 결과에 따라 boolean return
const result2 = arr.every(elem => elem %2 ===0)
console.log(result2)

// find Ex1.
// PEOPLE 중에 admin 권한을 가진 요소를 찾아서 admin 상수에 저장해보자!

const PEOPLE = [
  { id:1, admin: false },
  { id:2, admin: false },
  { id:3, admin: true },
]

const person = PEOPLE.find(function(person) {
  return person.admin === true
})

console.log(person)
*/

// some & every Ex1.
const COMPUTERS = [
  { name: 'macbook', ram: 16 },
  { name: 'gram', ram: 8 },
  { name: 'series9', ram: 32 },
]

//1. some
const someComputersAvailable  = COMPUTERS.some(function(computer) {
  return computer.ram > 16
})

console.log(someComputersAvailable)

//2. every
const everyComputersAvailable  = COMPUTERS.every(function(computer){
  return computer.ram > 16
})
console.log(everyComputersAvailable)