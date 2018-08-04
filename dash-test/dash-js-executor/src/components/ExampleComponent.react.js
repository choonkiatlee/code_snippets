import React,{Component} from 'react';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class JSExecutor extends Component {
   
    render() {

        const {text, setProps, src} = this.props;

        var func = new Function("return " + src)();
        if (setProps){
            setProps({
                //text:func(this.props.input)
                text: 'Hello'
            });
        }

        {text};
        

        return null
    }
}       

JSExecutor.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Input Javascript Source
     */

    src: PropTypes.string,      

    /**
     * Input to JS Script
     */
    input: PropTypes.any,


    /**
     * Text to be rendered in event
     */
    text: PropTypes.string,


    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func



};
