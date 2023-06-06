import DiaryItem from "./DiaryItem";

const DiaryList = ({ diaryList, onDelete, onUpdate, onEdit, }) => {
  return (
    <div className="DiaryList">
      <h2>다이어리 리스트</h2>
      <h4>{diaryList.length}개의 일기 있다.</h4>
      <div>
        {diaryList.map((item) => (
          // 자식 요소는 고유한 key prop를 가지고 있어야 함.
          // <div key={item.id}>
          //   <div>작성자: {item.author} </div>
          //   <div>일기: {item.content} </div>
          //   <div>감정: {item.emotion} </div>
          //   <div>작성 시간(ms): {item.created_date} </div>
          // </div>
          <DiaryItem key={item.id} {...item} onDelete={onDelete} onUpdate={onUpdate} onEdit={onEdit}/>
        ))}
      </div>
    </div>
  );
};

DiaryList.defaultProps = {
  diaryList: [],
};

export default DiaryList;
