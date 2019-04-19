import React, {Component} from 'react';
import './ChangeGreeter.css'

class ChangeGreeter extends Component{
    constructor(props){
        super(props);
        this.state = {oldName: '', newName: ''};
        this.changeGreeting = this.changeGreeting.bind(this);
        this.handleOld = this.handleOld.bind(this);
        this.handleNew = this.handleNew.bind(this);

    }
    render(){
        return(
        <div className="ChangeGreeter">
            oldGreeting: <input type="text" onChange={this.handleOld}/>
            replace with: <input type="text" onChange={this.handleNew}/>

            <button onClick={this.changeGreeting}>Change </button>
        </div>
        );
    }
    handleOld(event){
        this.setState({oldName:event.target.value});
    }
    handleNew(event){
        this.setState({newName:event.target.value});
    }
    changeGreeting(){
        this.props.changeGreeting(this.state.oldName, this.state.newName);
        this.setState({oldName:'', newName:''});
    }
}
export default ChangeGreeter;
