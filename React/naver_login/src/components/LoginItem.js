import {useState} from "react";
import Toggle from "./Toggle";

function LoginItem() {
  const [inputs, setInputs] = useState({
    id: '',
    password: '',
  });

  const [isIdFocus, setIdFocus] = useState(false);
  const [isPasswordFocus, setPasswordFocus] = useState(false);
  const { id, password } = inputs;

  const handlechange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleDelete = (inputName) => {
    setInputs({ ...inputs, [inputName]: '' });
  };

  return (
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
            <div className="btn_delete" onClick={() => handleDelete('id')}>
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
      <div className="login_keep_wrap">
        <div className="keep_check">
          <input type="checkbox"></input>
          <label className="keep_text">로그인 상태 유지</label>
        </div>
        <div className="ip_check">
          <a href="https://nid.naver.com/login/ext/help_ip3.html">
            <span className="ip_text">IP보안</span>
          </a>
          <span class="toggle"><Toggle /></span>
        </div>
      </div>
      <div className="btn_login_wrap">
        <button className="btn_login" type="submit">
          <span className="btn_text">로그인</span>
        </button>
      </div>
    </form>
  );
};

export default LoginItem;
