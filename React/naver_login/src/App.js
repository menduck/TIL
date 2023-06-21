import { useState } from 'react';
import './App.css';
import logo from './logo.svg';

function App() {
  const [inputs, setInputs] = useState({
    id: '',
    password: '',
  });

  // const [isFocus, setFocus] = useState({
  //   id: false,
  //   password: false,
  // })
  const [isIdFocus, setIdFocus] = useState(false)
  const [isPasswordFocus, setPasswordFocus] = useState(false)
  const { id, password } = inputs;

  const handlechange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleDelete = (inputName) => {
    setInputs({ ...inputs, [inputName]: '' });
  };

  return (
    <>
      <header>
        <img src={logo} className="logo" alt="logo" />
      </header>
      <div className="content__container">
        <div className="login__wrap">
          <ul className="menu_wrap">
            <li className="menu_item">
              <span className="menu_text">ID 로그인</span>
            </li>
            <li className='menu_item'>
            <span className='menu_text'>일회용 번호</span>
          </li>
          <li className='menu_item'>
            <span className='menu_text'>QR코드</span>
          </li>
          </ul>
          <ul className="panel_wrap">
            <div className="panel_inner">
              <form>
                <div className="id_pw_wrap">
                  <div className={`input_row ${isIdFocus ? 'focus' : ''}`}>
                    <input
                      type="text"
                      placeholder="아이디"
                      name="id"
                      className="input_text"
                      maxLength="41"
                      onChange={handlechange}
                      onFocus={() => setIdFocus(true)}
                      onBlur={() => setIdFocus(false)}
                      value={inputs.id}
                    />
                    {id && (
                      <div
                        className="btn_delete"
                        onClick={() => handleDelete('id')}
                      >
                        X
                      </div>
                    )}
                  </div>
                  <div className={`input_row ${isPasswordFocus ? 'focus' : ''}`}>
                    <input
                      type="password"
                      placeholder="비밀번호"
                      name="password"
                      className="input_text"
                      maxLength="16"
                      onChange={handlechange}
                      onFocus={() => setPasswordFocus(true)}
                      onBlur={() => setPasswordFocus(false)}
                      value={inputs.password}
                    />
                    {password && (
                      <div
                        className="btn_delete"
                        onClick={() => handleDelete('password')}
                      >
                        X
                      </div>
                    )}
                  </div>
                </div>
                <div className="btn_login_wrap">
                  <button className="btn_login" type="submit">
                    <span className="btn_text">로그인</span>
                  </button>
                </div>
              </form>
            </div>
          </ul>
        </div>
        <ul className='find_wrap'>
          <li>
            <a className='find_text' href='https://nid.naver.com/user2/help/pwInquiry?lang=ko_KR'>비밀번호 찾기</a>
          </li>
          <li>
            <a className='find_text' href='https://nid.naver.com/user2/help/idInquiry?lang=ko_KR'>아이디 찾기</a>
          </li>
          <li>
            <a className='find_text' href='https://nid.naver.com/user2/join/agree?lang=ko_KR&domain=www.naver.com'>회원가입</a>
          </li>
        </ul>
      </div>
    </>
  );
}

export default App;
