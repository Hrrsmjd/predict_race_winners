import { Link } from 'react-router-dom'
import '../App.css';

function Navbar() {
  return (
    <div className="Notebook">
      <nav>
          <h2> Predict Race Winners </h2>
          <ul className="Navlist">
              <Link to="/"><li className='Button'> Home </li></Link>
              <Link to="/howto"><li className='Button'> How to </li></Link>
              <Link to="/predict"><li className='Button'> Predict </li></Link>
          </ul>
      </nav>
    </div>
  );
}

export default Navbar;
