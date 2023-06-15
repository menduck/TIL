import { useRef, useState } from 'react';
import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';

// const dumpList = [
//   {
//     id: 1,
//     author: '김미넛',
//     content: '오늘',
//     emotion: 3,
//     created_date: new Date().getTime(),
//   },
//   {
//     id: 2,
//     author: '승우야',
//     content: '오늘',
//     emotion: 5,
//     created_date: new Date().getTime(),
//   },
//   {
//     id: 3,
//     author: '아아요',
//     content: '오늘',
//     emotion: 2,
//     created_date: new Date().getTime(),
//   },
//   {
//     id: 4,
//     author: '김시여',
//     content: '오늘',
//     emotion: 1,
//     created_date: new Date().getTime(),
//   },
// ];

function App() {
  const [data, setData] = useState([]);
  const dataId = useRef(0);
  const onCreate = (author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current,
    };
    dataId.current += 1;
    setData([newItem, ...data])
  };

  const onDelete = (targetId) => {
    console.log(`${targetId}가 삭제되었습니다.`)
    const newDiarytList = data.filter((item) => item.id !== targetId)
    setData(newDiarytList)
  }

  const onUpdate = (targetContent) => {
    console.log(`${targetContent}의 내용 수정`)
  }

  // 데이터 (위 -> 아래), 이벤트는 (아래 -> 위)
  // 수정 이벤트(DiaryItem)를 앱 컴포넌트까지 전달하기 위해서, 데이터를 가지고 있는 앱 컴포넌트에서 데이터를 DiaryItem까지 보내줘야 한다.
  
  const onEdit = (targetId, newContent) => {
    console.log(targetId, newContent)
  }

  return (
    <div className="App">
      <DiaryEditor onCreate={onCreate} />
      <DiaryList diaryList={data} onDelete={onDelete} onUpdate={onUpdate} onEdit={onEdit}/>
    </div>
  );
}

export default App;
