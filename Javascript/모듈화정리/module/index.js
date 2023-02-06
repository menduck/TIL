/* 방법1
import { perfectScore,sum,avg } from "./math.js";

console.log('perfectScore',perfectScore)
console.log('sum: ',sum(10,20))
console.log('avg: ',avg(40,80))

*/

/* 별칭을 이용해서 import하는 방법
import * as math from './math.js';
console.log('perfectScore',math.perfectScore)
console.log('sum: ',math.sum(10,20))
console.log('avg: ',math.avg(40,80))
*/

// export default를 사용하여 내보내는 방법 단, 모듈당 하나만 가능.
// 이름을 마음대로 지정 가능

import subtract from './math.js'
import subtract222 from './math.js'
console.log('subtract: ',subtract(20,10));
console.log('subtract: ',subtract222(20,10));