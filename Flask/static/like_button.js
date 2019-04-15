import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

'use strict';

const e = React.createElement;


const styles = theme => ({
  margin: {
    margin: theme.spacing.unit,
  },
  extendedIcon: {
    marginRight: theme.spacing.unit,
  },
});

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      history.replaceState({id: 'homepage'}, "litpage", "end.html");
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}
function ButtonSizes(props) {
    const { classes } = props;
    return ( <div>
        <Button variant="outlined" size="medium" color="primary" className={classes.margin}>
        hi! it's react
        </div>);
}

const domContainer = document.querySelector('#react');
ReactDOM.render(e(LikeButton), domContainer);
ReactDOM.render(<Demo />, document.querySelector('#root'));
