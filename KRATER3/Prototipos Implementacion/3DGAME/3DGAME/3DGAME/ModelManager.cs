using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;


namespace _3DGAME {

    public class ModelManager : DrawableGameComponent {

        List<basicModel> models = new List<basicModel>();

        protected override void LoadContent() {
            models.Add(new basicModel(
            Game.Content.Load<Model>(@"models\cartoontreeFBX")));
            base.LoadContent();
        }

        public ModelManager(Game game) : base(game) {
        }

        public override void Initialize() {
            base.Initialize();
        }

        public override void Update(GameTime gameTime) {
            for (int i = 0; i < models.Count; ++i) {
                models[i].Update();
            }
            base.Update(gameTime);
        }

        public override void Draw(GameTime gameTime) {
            foreach (basicModel bm in models) {
                bm.Draw(((Game1)Game).camera);
            }
            base.Draw(gameTime);
        }

    }
}
