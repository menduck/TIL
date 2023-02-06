
/* 방법1 
const {perfectScore,sum,avg,subtract} = require('./math.js');

console.log('perfectScore',perfectScore);
console.log('sum: ',sum(10,20));
console.log('avg: ',avg(40,80));
console.log('subtract: ',subtract(20,10));
*/

// 하나의 객체로 한번에 받는 방법
const math = require('./math.js');

console.log('perfectScore',math.perfectScore);
console.log('sum: ',math.sum(10,20));
console.log('avg: ',math.avg(40,80));
console.log('subtract: ',math.subtract(20,10));
