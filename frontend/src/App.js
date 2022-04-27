import './App.css';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import { BrowserRouter as Router, Route} from "react-router-dom";


const App = () => {
    return (
        <div className='App'>
            <Router>
                <Route component={HomePage} path='/' exact />
                <Route component={LoginPage} path='login/' />
            </Router>
        </div>
    );
}

export default App;
