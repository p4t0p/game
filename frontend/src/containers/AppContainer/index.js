import React, {Suspense} from 'react';

import Button from 'atol-atoms/Button';
import Loader from 'atol-atoms/Loader';

import './style.scss';

export default function AppContainer() {
    const [data, setData] = React.useState(localStorage.getItem('data'))
    const [isLoading, setIsisLoading] = React.useState(!Boolean(data));

    React.useEffect(() => {
        if (!data || data === null) {
            setIsisLoading(true);
            fetch('http://localhost:8080/game', {method: 'POST'})
                .then(r => r.json())
                .then(data => {
                    setData(data)
                    setIsisLoading(false);
                })
        }
    }, []);

    console.log('data', data);

    if (isLoading) {
        return <Loader active />;
    }

    let sC = 'bg-white';

    return (
        <div className="AppContainer">
            <Button >Новая игра</Button>
            <div className="Field">
            {
                data.field.map(row => {
                    return (
                        <div className="Row">
                        {
                            row.map(cell => {
                                return (
                                    <div
                                        className={`Cell ${cell && cell.kind} ${cell && cell.color}`}
                                    />
                                )
                            })
                        }
                        </div>
                    );
                })
            }
            </div>
        </div>

    )
}
