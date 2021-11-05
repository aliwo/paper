import sql from 'k6/x/sql';

const db = sql.open('mysql', 'mysql://root:22380476@127.0.0.1/paper?charset=UTF8MB4');

export function setup() {

}

export function teardown() {
    db.close();
}

export default function () {
    db.exec('SELECT NOW();');
    let result = sql.query(db, 'SELECT NOW();');
    console.log(result);
}



