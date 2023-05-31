import { useRef, useState } from 'react';

// 작성자, 일기 본문, 감정 점수를 입력받는 컴포넌트
const DiaryEditor = () => {
  // 동작이 비슷한 state이기 때문에 하나의 state로 묶을 수 있음.
  // const [author, setAuthor] = useState('');
  // const [content, setContent] = useState('');

  const [state, setState] = useState({ author: '', content: '', emotion: 1 });

  const handleChangeState = (e) => {
    setState({
      ...state,
      [e.target.name]: e.target.value,
    });
  };

  const authorInput = useRef();
  const contentInput = useRef();

  const handleSubmit = () => {
    if (state.author.length < 1) {
      authorInput.current.focus();

      // 더 이상 진행되지 않도록 return시킴
      return;
    }

    if (state.content.length < 5) {
      contentInput.current.focus();
      return;
    }

    alert('저장 성공');
  };

  return (
    <div className="DiaryEditor">
      <h2>오늘의 일기</h2>
      <div>
        <input
          ref={authorInput}
          name="author"
          // value={author}
          value={state.author}
          onChange={handleChangeState}
          // onChange={(e) => {
          // author가 변화되는 값 => e.target.value
          // 이벤트가 발생한 target element의 이름값 => e.target.name

          // author 값이 업데이트 될때마다 업데이트 시켜줌
          // setAuthor(e.target.value);

          // setState({
          //   // 스프레드 연산자도 state가 가지고 있는 props을 가져옴
          //   ...state,
          //   author: e.target.value,

          // 다 나열할 순 있지만, 여러 개이면 일일이 작성하기 어렵기 때문에 스프레드 연산자를 사용함.
          // content: state.content
          // });
          // }}
        />
      </div>
      <div>
        <textarea
          ref={contentInput}
          name="content"
          // value={content}
          value={state.content}
          onChange={handleChangeState}
          // onChange={(e) =>
          // setContent(e.target.value)
          // setState({
          //   ...state,
          //   content: e.target.value,
          // author: state.author
          // })
          // }
        />
      </div>
      <div>
        오늘의 감정 점수 :
        <select
          name="emotion"
          value={state.emotion}
          onChange={handleChangeState}
        >
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
          <option value={5}>5</option>
        </select>
      </div>
      <div>
        <button onClick={handleSubmit}>일기 저장하기</button>
      </div>
    </div>
  );
};

export default DiaryEditor;
