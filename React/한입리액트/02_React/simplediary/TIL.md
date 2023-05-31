<!-- # useState

```js
const [state, setState] = useState(initialState);
```

- 관례적으로, 배열 비구조 분해로 state 변수를 지정함.
- state에는 상태값, setState는 업데이트 값을 넣 -->

# useRef

```js
const ref = useRef(initialValue)
```

- 컴포넌트의 재렌더링 사이에서 지속되는 변경 가능한 참조를 생성할 수 있게 해줌.
- current라는 속성을 갖는 변경 가능한 참조 객체를 반환함.

```js
// DiaryEditor.js
import { useRef } from 'react';

const DiaryEditor = () => {
  const authorInput = useRef();

  const handleSubmit = () => {
    if (state.author.length < 1) {
      authorInput.current.focus();

      // 더 이상 진행되지 않도록 return시킴
      return;
    }
    alert('저장 성공');
  };

  return (
    <div className="DiaryEditor">
      <div>
        <input ref={authorInput}>
      </div>
      <div>
        <button onClick={handleSubmit}>일기 저장하기</button>
      </div>
    </div>
  )
}
```

- input DOM을 선택하려면,
1. useRef()를 호출해서 Ref 객체 생성
2. input 요소에  ref 속성을 추가하고, 그 값으로 useRef에서 생성한 Ref 객체를 설정함. =>  Ref 객체와 input 요소가 연결
3. Ref객체.current 를 사용해, 선택한 DOM 요소에 직접 접근이 가능함.