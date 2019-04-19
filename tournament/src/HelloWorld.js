import React, {Component} from 'react';
import './HelloWorld.css';

// const HelloWorld = props => {
//     return(<div className="HelloWorld">tournament for {props.name}!!!!</div>); // css classname of App
// };

class HelloWorld extends Component {
    constructor(props){
        super(props);
        this.state = { greeting: "hello!"};
        this.frenchify = this.frenchify.bind(this);
        this.removeGreeting = this.removeGreeting.bind(this);
    }

    render() {
      return (
        <div className="HelloWorld">
          {this.state.greeting} {this.props.name}!
          <br/>
          <button onClick={this.frenchify}>Frenchify!</button>
          <br/>
          <button onClick={this.removeGreeting}>Remove Me!</button>
        </div>
      );
    }

    frenchify() {
        this.setState( {greeting : "bonjour"});
    }

    removeGreeting(){
        this.props.removeGreeting(this.props.name);
    }

}

export default HelloWorld;
