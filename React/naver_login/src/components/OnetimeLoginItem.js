import { useState } from "react";

function OnetimeLoginItem() {
  const [onetimeNum, setOnetimeNum] = useState('')
  const [isOnetimeNumFocus, setOnetimeNumFocus] = useState(false);

  const handleOnchange = (e) => {
    setOnetimeNum(e.target.value)
  }

  const handleOnDelete = () => {
    setOnetimeNum('')
  }

  return (
    <>
    <div className="help_text">
      네이버앱의 메뉴 > 설정  > 로그인 아이디 관리 > 더보기  > 일회용 로그인 번호에 보이는 번호를 입력해 주세요.
    </div>
    <div className={`input_row ${isOnetimeNumFocus ? 'focus' : ''}`}>
          <input
            type="text"
            placeholder="번호를 입력하세요."
            name="id"
            className="input_text"
            onChange={handleOnchange}
            onFocus={() => setOnetimeNumFocus(true)}
            onBlur={() => setOnetimeNumFocus(false)}
            value={onetimeNum}
          />
          {onetimeNum && (
            <div className="btn_delete" onClick={handleOnDelete}>
              X
            </div>
          )}
        </div>
    <div className="btn_login_wrap">
      <button className="btn_login" type="submit">
        <span className="btn_text">로그인</span>
      </button>
    </div>
    </>
  );
}

export default OnetimeLoginItem;
