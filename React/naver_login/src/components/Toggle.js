import { useState } from 'react';

const Toggle = () => {
  const [isOn, setIsOn] = useState(false);

  const toggleHandler = () => {
    setIsOn(!isOn);
  };

  return (
    <>
      <div className="toggleWrap" onClick={toggleHandler}>
        <div
          className={`toggle-container ${isOn ? 'toggle-checked' : null}`}
        ></div>
        <div
          className={`toggle-circle ${isOn ? 'toggle-circle-checked' : null}`}
        ></div>
      </div>
    </>
  );
};

export default Toggle;
