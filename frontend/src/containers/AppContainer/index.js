import React, {Suspense} from 'react';

import Button from 'atol-atoms/Button';
import Loader from 'atol-atoms/Loader';

import './style.scss';

function Field({field, makeMove, turn}) {
    const [activeCell, setActiveCell] = React.useState(null);

    const select = (id, cell) => {
        if (!activeCell && !cell) {
            return;
        }
        if (!activeCell && cell.color !== turn) {
            return
        }
        if (activeCell && id === activeCell[0]) {
            setActiveCell(null)
        } else {
            if (activeCell) {
                const [_, y, x] = id.split('.').map(Number);
                makeMove(
                    {x: activeCell[1].x, y: activeCell[1].y},
                    {x, y}
                )
                setActiveCell(null)
            } else {
                setActiveCell([id, cell]);
            }
        }
    }

    const rows = field.map((row, j) => {
        return (
            <div className="Row" key={'r' + j}>
            {
                row.map((cell, i) => {
                    const id = `C.${j}.${i}`
                    const cellColor = j % 2 ? (i % 2 ? 'white' : 'black') : (i % 2 ? 'black' : 'white');
                    const className = `Cell ${cell && cell.kind} ${cell && cell.color} bg-${cellColor} ${activeCell && activeCell[0] === id ? 'active' : ''}`;
                    return <div key={id} cid={id} className={className} onClick={() => select(id, cell)} />
                })
            }
            </div>
        );
    });

    return (
        <div className={`Field ${activeCell && 'active'} turn-${turn}`}>
            {rows}
        </div>
    );
}

export default function AppContainer() {
    const [data, setData] = React.useState(localStorage.getItem('data'))
    const [isLoading, setIsisLoading] = React.useState(!Boolean(data));

    const start = () => {
        setIsisLoading(true);
            fetch('http://localhost:8080/game', {method: 'POST'})
                .then(r => r.json())
                .then(data => {
                    setData(data)
                    setIsisLoading(false);
                })
                .catch(error => {
                    console.error(error);
                })
    }

    React.useEffect(() => {
        if (!data || data === null) {
            start();
        }
    }, []);

    function makeMove(_from, _to) {
        setIsisLoading(true);
        fetch('http://localhost:8080/move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({...data, move: {
                from: _from,
                to: _to,
            }})
        })
            .then(r => r.json())
            .then(data => {
                if (data.error) {
                    alert(data.error)
                } else {
                    setData(data)
                }
                setIsisLoading(false);
            })
    }

    if (isLoading) {
        return <Loader active />;
    }

    return (
        <div className="AppContainer">
            <Button onClick={start}>Новая игра</Button>
            <Field field={data.field} turn={data.turn} makeMove={makeMove} />
        </div>

    )
}
