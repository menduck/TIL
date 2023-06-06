import { useState } from 'react';

const DiaryItem = ({
  author,
  content,
  created_date,
  emotion,
  id,
  onDelete,
  onEidt,

}) => {
  const handleRemove = () => {
    if (window.confirm(`${id + 1}번째 일기를 삭제하시겠습니까?`)) {
      onDelete(id);
    }
  };

  const [isEdit, setIsEdit] = useState(false);
  const toggleIsEdit = () => setIsEdit(!isEdit);
  const [localContent, setLocalContent] = useState(content);
  const handleQuitEdit = () => {
    setIsEdit(false);
    setLocalContent(content)
  };
  const handleSave = () => {
    onEidt(id, localContent)
  }
  return (
    <div className="DiaryItem">
      <div className="info">
        <span>
          작성자 : {author} | 감정점수 : {emotion}
        </span>
        <div className="date">
          날짜 : {new Date(created_date).toLocaleString()}
        </div>
        <div className="content">
          {isEdit ? (
            <>
              <textarea
                value={localContent}
                onChange={(e) => setLocalContent(e.target.value)}
              />
            </>
          ) : (
            <>{content}</>
          )}
        </div>

        {isEdit ? (
          <>
            <button onClick={handleQuitEdit}>취소</button>
            <button onClick={handleSave}>수정 완료</button>
          </>
        ) : (
          <>
            <button onClick={handleRemove}>삭제하기</button>
            <button onClick={toggleIsEdit}>수정하기</button>
          </>
        )}
      </div>
    </div>
  );
};

export default DiaryItem;
